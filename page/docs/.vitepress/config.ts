import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/qlibAssistant/',
  metaChunk: true,
  title: 'qlib csi300 score',
  description: 'qlib 量化选股评分数据展示',
  lang: 'zh-CN',
  themeConfig: {
    socialLinks: [
      { icon: 'github', link: 'https://github.com/touhoufan2024/qlibAssistant' },
    ],
    nav: [
      { text: '首页', link: '/' },
      { text: 'qlib中文教程', link: '/pages/notes/' },
      { text: '文档', link: '/pages/essays/' },
      { text: '帮助', link: '/pages/about' },
    ],
    sidebar: [
      {
        text: '数据目录',
        link: '/',
        items: [{ text: 'selection_20260310_17_37_47', link: '/score/selection_20260310_17_37_47/' },
      { text: 'selection_20260309_15_48_03', link: '/score/selection_20260309_15_48_03/' },
      { text: 'selection_20260308_21_11_10', link: '/score/selection_20260308_21_11_10/' },
      { text: 'selection_20260308_18_24_44', link: '/score/selection_20260308_18_24_44/' },
      { text: 'selection_20260308_16_54_35', link: '/score/selection_20260308_16_54_35/' },
      { text: 'selection_20260307_18_13_28', link: '/score/selection_20260307_18_13_28/' },
      { text: 'selection_20260307_14_52_24', link: '/score/selection_20260307_14_52_24/' },
      { text: 'selection_20260306_14_23_13', link: '/score/selection_20260306_14_23_13/' },
      { text: 'selection_20260306_08_46_19', link: '/score/selection_20260306_08_46_19/' },
      { text: 'selection_20260306_07_50_36', link: '/score/selection_20260306_07_50_36/' },
      { text: 'selection_20260305_14_15_34', link: '/score/selection_20260305_14_15_34/' },
      { text: 'selection_20260304_14_10_59', link: '/score/selection_20260304_14_10_59/' },
      { text: 'selection_20260303_14_13_18', link: '/score/selection_20260303_14_13_18/' },
      { text: 'selection_20260302_14_14_32', link: '/score/selection_20260302_14_14_32/' },
      { text: 'selection_20260301_13_52_30', link: '/score/selection_20260301_13_52_30/' },
      { text: 'selection_20260228_13_51_02', link: '/score/selection_20260228_13_51_02/' },
      { text: 'selection_20260227_14_14_17', link: '/score/selection_20260227_14_14_17/' },
      { text: 'selection_20260226_14_24_10', link: '/score/selection_20260226_14_24_10/' },
      { text: 'selection_20260225_14_23_08', link: '/score/selection_20260225_14_23_08/' },
      { text: 'selection_20260224_14_24_14', link: '/score/selection_20260224_14_24_14/' },
      { text: 'selection_20260223_14_21_13', link: '/score/selection_20260223_14_21_13/' },
      { text: 'selection_20260222_13_59_11', link: '/score/selection_20260222_13_59_11/' },
      { text: 'selection_20260222_08_26_09', link: '/score/selection_20260222_08_26_09/' },
      { text: 'selection_20260221_13_56_25', link: '/score/selection_20260221_13_56_25/' },
      { text: 'selection_20260221_06_03_18', link: '/score/selection_20260221_06_03_18/' },
      { text: 'selection_20260220_14_13_44', link: '/score/selection_20260220_14_13_44/' },
      { text: 'selection_20260220_09_45_38', link: '/score/selection_20260220_09_45_38/' },
      { text: 'selection_20260220_09_14_05', link: '/score/selection_20260220_09_14_05/' },
      { text: 'selection_20260220_05_42_48', link: '/score/selection_20260220_05_42_48/' },
      { text: 'selection_20260219_14_23_49', link: '/score/selection_20260219_14_23_49/' },
      { text: 'selection_20260218_14_21_28', link: '/score/selection_20260218_14_21_28/' },
      { text: 'selection_20260217_14_21_25', link: '/score/selection_20260217_14_21_25/' },
      { text: 'selection_20260216_14_18_53', link: '/score/selection_20260216_14_18_53/' },
      { text: 'selection_20260215_14_02_04', link: '/score/selection_20260215_14_02_04/' },
      { text: 'selection_20260214_14_00_30', link: '/score/selection_20260214_14_00_30/' },
      { text: 'selection_20260213_14_16_00', link: '/score/selection_20260213_14_16_00/' },
      { text: 'selection_20260212_14_25_13', link: '/score/selection_20260212_14_25_13/' },
      { text: 'selection_20260211_18_07_57', link: '/score/selection_20260211_18_07_57/' },
      { text: 'selection_20260211_17_29_45', link: '/score/selection_20260211_17_29_45/' }],
      },
    ],
    outline: {
      level: [2, 3],
    },
    footer: {
      message: (() => {
        const now = new Date()
        const dateTime = now.toLocaleString('zh-CN', {
          timeZone: 'UTC',
          year: 'numeric',
          month: 'numeric',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit',
          second: '2-digit',
          hour12: false,
        }) + ' UTC'
        const parts = [`生成日期: ${dateTime}`]
        const os =
          process.env.RUNNER_OS ||
          process.env.OS ||
          { win32: 'Windows', darwin: 'macOS', linux: 'Linux' }[process.platform] ||
          process.platform
        const runId = process.env.GITHUB_RUN_ID
        parts.push(`运行环境: ${os}`)
        if (runId) parts.push(`构建 ID: ${runId}`)
        parts.push(`Node: ${process.version}`)
        return parts.join(' · ')
      })(),
    },
  },
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark',
    },
  },
})
