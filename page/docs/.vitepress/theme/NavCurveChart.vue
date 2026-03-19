<template>
  <div>
    <div class="kpi-bar">
      <div v-for="kpi in kpis" :key="kpi.label" class="kpi-card">
        <div class="kpi-label">{{ kpi.label }}</div>
        <div class="kpi-value">{{ kpi.value }}</div>
      </div>
    </div>

    <div class="legend">
      <span class="legend-item"><i class="legend-dot strategy"></i>策略净值</span>
      <span class="legend-item"><i class="legend-dot benchmark"></i>CSI300净值</span>
      <span class="legend-item"><i class="legend-dot drawdown"></i>水下回撤</span>
    </div>

    <div ref="hostEl" class="chart-host"></div>
    <p class="chart-status">{{ statusText }}</p>
  </div>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from "vue";
import { createChart, LineSeries, AreaSeries, CrosshairMode } from "lightweight-charts";

const props = defineProps({
  strategy: {
    type: String,
    required: true,
  },
});

const hostEl = ref(null);
const statusText = ref("正在加载图表...");
const kpis = ref([
  { label: "策略累计", value: "--" },
  { label: "基准累计", value: "--" },
  { label: "超额累计", value: "--" },
  { label: "策略年化", value: "--" },
  { label: "最大回撤", value: "--" },
  { label: "日胜率", value: "--" },
]);

let mainChart = null;
let ddChart = null;
let resizeHandler = null;

const COLORS = {
  strategy: "#2563eb",
  benchmark: "#ef4444",
  drawdownLine: "#475569",
  drawdownTop: "rgba(71, 85, 105, 0.30)",
  drawdownBottom: "rgba(71, 85, 105, 0.06)",
};

function resolveDataUrl(path) {
  const base = (import.meta.env.BASE_URL || "/").replace(/\/+$/, "");
  return `${base}${path.startsWith("/") ? path : `/${path}`}`;
}

function dateToTs(dateStr) {
  const d = new Date(`${String(dateStr).slice(0, 10)}T00:00:00Z`);
  return Math.floor(d.getTime() / 1000);
}

function fmtPct(x) {
  return Number.isFinite(x) ? `${(x * 100).toFixed(2)}%` : "--";
}

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/).filter(Boolean);
  if (lines.length < 2) return [];
  const headers = lines[0].split(",");
  const rows = [];
  for (const line of lines.slice(1)) {
    const cols = line.split(",");
    const row = {};
    headers.forEach((h, i) => {
      row[h] = cols[i] ?? "";
    });
    rows.push(row);
  }
  return rows;
}

function buildSeries(rows) {
  const strategy = [];
  const benchmark = [];
  for (const row of rows) {
    const time = dateToTs(row.date);
    const s = Number(row.strategy_equity);
    const b = Number(row.csi300_equity);
    if (Number.isFinite(time) && Number.isFinite(s)) {
      strategy.push({ time, value: s });
    }
    if (Number.isFinite(time) && Number.isFinite(b)) {
      benchmark.push({ time, value: b });
    }
  }
  strategy.sort((x, y) => x.time - y.time);
  benchmark.sort((x, y) => x.time - y.time);
  return { strategy, benchmark };
}

function calcDrawdown(series) {
  let maxVal = -Infinity;
  return series.map((p) => {
    if (p.value > maxVal) maxVal = p.value;
    return { time: p.time, value: maxVal > 0 ? p.value / maxVal - 1 : 0 };
  });
}

function calcKpis(strategy, benchmark, drawdown) {
  if (!strategy.length) return;
  const s0 = strategy[0].value;
  const sN = strategy[strategy.length - 1].value;
  const b0 = benchmark.length ? benchmark[0].value : NaN;
  const bN = benchmark.length ? benchmark[benchmark.length - 1].value : NaN;
  const n = strategy.length;

  const strategyCum = sN / s0 - 1;
  const benchmarkCum = Number.isFinite(b0) && Number.isFinite(bN) ? bN / b0 - 1 : NaN;
  const excessCum = Number.isFinite(benchmarkCum) ? strategyCum - benchmarkCum : NaN;
  const strategyAnn = n > 1 ? Math.pow(sN / s0, 252 / (n - 1)) - 1 : NaN;
  const maxDd = drawdown.length ? Math.min(...drawdown.map((d) => d.value)) : NaN;

  let win = 0;
  let total = 0;
  if (benchmark.length && benchmark.length === strategy.length) {
    for (let i = 1; i < strategy.length; i += 1) {
      const sr = strategy[i].value / strategy[i - 1].value - 1;
      const br = benchmark[i].value / benchmark[i - 1].value - 1;
      if (Number.isFinite(sr) && Number.isFinite(br)) {
        total += 1;
        if (sr > br) win += 1;
      }
    }
  }
  const winRate = total > 0 ? win / total : NaN;

  kpis.value = [
    { label: "策略累计", value: fmtPct(strategyCum) },
    { label: "基准累计", value: fmtPct(benchmarkCum) },
    { label: "超额累计", value: fmtPct(excessCum) },
    { label: "策略年化", value: fmtPct(strategyAnn) },
    { label: "最大回撤", value: fmtPct(maxDd) },
    { label: "日胜率", value: fmtPct(winRate) },
  ];
}

function formatDate(ts) {
  const d = new Date(Number(ts) * 1000);
  const yyyy = d.getUTCFullYear();
  const mm = String(d.getUTCMonth() + 1).padStart(2, "0");
  const dd = String(d.getUTCDate()).padStart(2, "0");
  return `${yyyy}-${mm}-${dd}`;
}

onMounted(async () => {
  if (!hostEl.value) return;

  const shadowRoot = hostEl.value.attachShadow({ mode: "open" });
  const styleEl = document.createElement("style");
  styleEl.textContent = `
    .main-wrap {
      position: relative;
      width: 100%;
      height: 420px;
      border: 1px solid #e2e8f0;
      border-radius: 8px 8px 0 0;
      overflow: hidden;
      background: #ffffff;
    }
    .dd-wrap {
      width: 100%;
      height: 170px;
      border: 1px solid #e2e8f0;
      border-top: 0;
      border-radius: 0 0 8px 8px;
      overflow: hidden;
      background: #ffffff;
    }
    .overlay {
      position: absolute;
      top: 10px;
      left: 10px;
      z-index: 10;
      min-width: 280px;
      padding: 8px 10px;
      border-radius: 6px;
      border: 1px solid #dbe5f1;
      background: rgba(255, 255, 255, 0.92);
      color: #334155;
      font-size: 12px;
      line-height: 1.5;
      box-shadow: 0 1px 4px rgba(15, 23, 42, 0.08);
      pointer-events: none;
    }
    .date { font-weight: 600; margin-bottom: 2px; color: #0f172a; }
    .row {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      white-space: nowrap;
    }
    .k { color: #64748b; }
    .v { color: #0f172a; font-weight: 600; }
  `;

  const mainWrap = document.createElement("div");
  mainWrap.className = "main-wrap";
  const ddWrap = document.createElement("div");
  ddWrap.className = "dd-wrap";
  const overlay = document.createElement("div");
  overlay.className = "overlay";
  overlay.innerHTML = `
    <div class="date">--</div>
    <div class="row"><span class="k">策略净值</span><span class="v">--</span></div>
    <div class="row"><span class="k">CSI300净值</span><span class="v">--</span></div>
    <div class="row"><span class="k">超额</span><span class="v">--</span></div>
    <div class="row"><span class="k">回撤</span><span class="v">--</span></div>
  `;

  shadowRoot.appendChild(styleEl);
  shadowRoot.appendChild(mainWrap);
  shadowRoot.appendChild(ddWrap);
  mainWrap.appendChild(overlay);

  mainChart = createChart(mainWrap, {
    width: hostEl.value.clientWidth,
    height: 420,
    layout: { background: { color: "#ffffff" }, textColor: "#334155" },
    localization: { locale: "zh-CN", dateFormat: "yyyy-MM-dd" },
    grid: { vertLines: { color: "#eef2f7" }, horzLines: { color: "#eef2f7" } },
    rightPriceScale: { borderColor: "#e2e8f0" },
    timeScale: {
      visible: false,
      borderColor: "#e2e8f0",
      timeVisible: false,
      secondsVisible: false,
      barSpacing: 12,
      rightOffset: 2,
      fixLeftEdge: true,
      fixRightEdge: true,
    },
    crosshair: { mode: CrosshairMode.Normal },
  });

  ddChart = createChart(ddWrap, {
    width: hostEl.value.clientWidth,
    height: 170,
    layout: { background: { color: "#ffffff" }, textColor: "#334155" },
    localization: { locale: "zh-CN", dateFormat: "yyyy-MM-dd" },
    grid: { vertLines: { color: "#eef2f7" }, horzLines: { color: "#eef2f7" } },
    rightPriceScale: { borderColor: "#e2e8f0", scaleMargins: { top: 0.15, bottom: 0.12 } },
    timeScale: {
      visible: true,
      borderColor: "#e2e8f0",
      timeVisible: true,
      secondsVisible: false,
      barSpacing: 12,
      rightOffset: 2,
      fixLeftEdge: true,
      fixRightEdge: true,
    },
    crosshair: { mode: CrosshairMode.Normal },
  });

  const strategySeries = mainChart.addSeries(LineSeries, {
    title: `${props.strategy} strategy`,
    color: COLORS.strategy,
    lineWidth: 2,
  });
  const benchmarkSeries = mainChart.addSeries(LineSeries, {
    title: `${props.strategy} csi300`,
    color: COLORS.benchmark,
    lineWidth: 2,
  });
  const ddSeries = ddChart.addSeries(AreaSeries, {
    title: `${props.strategy} drawdown`,
    lineColor: COLORS.drawdownLine,
    topColor: COLORS.drawdownTop,
    bottomColor: COLORS.drawdownBottom,
    lineWidth: 1,
    priceFormat: { type: "price", precision: 2, minMove: 0.01 },
  });

  try {
    const res = await fetch(resolveDataUrl(`/backtest_csv/${props.strategy}.csv`));
    if (!res.ok) throw new Error(`读取 ${props.strategy}.csv 失败: ${res.status}`);
    const rows = parseCsv(await res.text());
    const { strategy, benchmark } = buildSeries(rows);
    if (!strategy.length || !benchmark.length) throw new Error("策略或基准数据为空");

    const drawdown = calcDrawdown(strategy);
    calcKpis(strategy, benchmark, drawdown);

    strategySeries.setData(strategy);
    benchmarkSeries.setData(benchmark);
    ddSeries.setData(drawdown.map((d) => ({ time: d.time, value: d.value * 100 })));
    mainChart.timeScale().fitContent();
    ddChart.timeScale().fitContent();

    const strategyMap = new Map(strategy.map((p) => [p.time, p.value]));
    const benchmarkMap = new Map(benchmark.map((p) => [p.time, p.value]));
    const drawdownMap = new Map(drawdown.map((p) => [p.time, p.value]));

    const updateOverlay = (time) => {
      const s = strategyMap.get(time);
      const b = benchmarkMap.get(time);
      const d = drawdownMap.get(time);
      const sText = Number.isFinite(s) ? s.toFixed(4) : "--";
      const bText = Number.isFinite(b) ? b.toFixed(4) : "--";
      const eText = Number.isFinite(s) && Number.isFinite(b) ? (s - b).toFixed(4) : "--";
      const dText = Number.isFinite(d) ? `${(d * 100).toFixed(2)}%` : "--";
      overlay.innerHTML = `
        <div class="date">${formatDate(time)}</div>
        <div class="row"><span class="k">策略净值</span><span class="v">${sText}</span></div>
        <div class="row"><span class="k">CSI300净值</span><span class="v">${bText}</span></div>
        <div class="row"><span class="k">超额</span><span class="v">${eText}</span></div>
        <div class="row"><span class="k">回撤</span><span class="v">${dText}</span></div>
      `;
    };

    const last = strategy[strategy.length - 1];
    if (last) updateOverlay(last.time);

    mainChart.subscribeCrosshairMove((param) => {
      if (!param || !param.time) return;
      updateOverlay(param.time);
    });
    ddChart.subscribeCrosshairMove((param) => {
      if (!param || !param.time) return;
      updateOverlay(param.time);
    });

    let syncing = false;
    mainChart.timeScale().subscribeVisibleLogicalRangeChange((range) => {
      if (syncing || !range) return;
      syncing = true;
      ddChart.timeScale().setVisibleLogicalRange(range);
      syncing = false;
    });
    ddChart.timeScale().subscribeVisibleLogicalRangeChange((range) => {
      if (syncing || !range) return;
      syncing = true;
      mainChart.timeScale().setVisibleLogicalRange(range);
      syncing = false;
    });

    statusText.value = `已加载：${props.strategy}`;
  } catch (err) {
    console.error("加载策略图失败:", err);
    statusText.value = `加载失败：${String(err)}`;
  }

  resizeHandler = () => {
    if (!hostEl.value || !mainChart || !ddChart) return;
    mainChart.resize(hostEl.value.clientWidth, 420);
    ddChart.resize(hostEl.value.clientWidth, 170);
  };
  window.addEventListener("resize", resizeHandler);
});

onBeforeUnmount(() => {
  if (resizeHandler) window.removeEventListener("resize", resizeHandler);
  if (mainChart) mainChart.remove();
  if (ddChart) ddChart.remove();
});
</script>

<style scoped>
.kpi-bar {
  display: grid;
  grid-template-columns: repeat(6, minmax(110px, 1fr));
  gap: 10px;
  margin-bottom: 10px;
}

.kpi-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 8px 10px;
  background: var(--vp-c-bg);
}

.kpi-label {
  font-size: 12px;
  color: var(--vp-c-text-2);
}

.kpi-value {
  margin-top: 2px;
  font-size: 15px;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

.legend {
  display: inline-flex;
  gap: 12px;
  margin-bottom: 10px;
  font-size: 12px;
  color: var(--vp-c-text-2);
}

.legend-item {
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.legend-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}

.legend-dot.strategy { background: #2563eb; }
.legend-dot.benchmark { background: #ef4444; }
.legend-dot.drawdown { background: #475569; }

.chart-host { width: 100%; }

.chart-status {
  margin-top: 8px;
  color: var(--vp-c-text-2);
  font-size: 13px;
}

@media (max-width: 1100px) {
  .kpi-bar {
    grid-template-columns: repeat(3, minmax(120px, 1fr));
  }
}
</style>
