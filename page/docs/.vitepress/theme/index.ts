import DefaultTheme from 'vitepress/theme'
import Layout from './Layout.vue'
import NavCurveChart from './NavCurveChart.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('NavCurveChart', NavCurveChart)
  },
}
