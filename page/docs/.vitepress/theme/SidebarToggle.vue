<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const STORAGE_KEY = 'vp-sidebar-collapsed'

const collapsed = ref(false)

function toggle() {
  collapsed.value = !collapsed.value
  applyState()
  try {
    localStorage.setItem(STORAGE_KEY, String(collapsed.value))
  } catch (_) {}
}

function applyState() {
  if (typeof document === 'undefined') return
  const el = document.documentElement
  if (collapsed.value) {
    el.classList.add('sidebar-collapsed')
  } else {
    el.classList.remove('sidebar-collapsed')
  }
}

onMounted(() => {
  try {
    collapsed.value = localStorage.getItem(STORAGE_KEY) === 'true'
  } catch (_) {
    collapsed.value = false
  }
  applyState()
})

onUnmounted(() => {
  document.documentElement.classList.remove('sidebar-collapsed')
})
</script>

<template>
  <button
    type="button"
    class="sidebar-toggle"
    :title="collapsed ? '展开侧边栏' : '收起侧边栏'"
    @click.stop.prevent="toggle"
  >
    <svg
      v-if="collapsed"
      xmlns="http://www.w3.org/2000/svg"
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <line x1="3" y1="12" x2="21" y2="12" />
      <line x1="3" y1="6" x2="21" y2="6" />
      <line x1="3" y1="18" x2="21" y2="18" />
    </svg>
    <svg
      v-else
      xmlns="http://www.w3.org/2000/svg"
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <line x1="3" y1="12" x2="21" y2="12" />
      <line x1="3" y1="6" x2="12" y2="6" />
      <line x1="3" y1="18" x2="12" y2="18" />
    </svg>
  </button>
</template>

<style scoped>
.sidebar-toggle {
  display: none;
}

@media (min-width: 960px) {
  .sidebar-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    padding: 0;
    margin-right: 8px;
    border: none;
    border-radius: 6px;
    background: transparent;
    color: var(--vp-c-text-2);
    cursor: pointer;
    transition: color 0.25s, background 0.25s;
  }

  .sidebar-toggle:hover {
    color: var(--vp-c-brand-1);
    background: var(--vp-c-default-soft);
  }
}
</style>
