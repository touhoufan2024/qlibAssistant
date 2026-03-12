<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { giscusConfig } from './giscus.config'

const container = ref<HTMLElement | null>(null)

onMounted(() => {
  if (!container.value || !giscusConfig.categoryId) return

  const script = document.createElement('script')
  script.src = 'https://giscus.app/client.js'
  script.setAttribute('data-repo', giscusConfig.repo)
  script.setAttribute('data-repo-id', giscusConfig.repoId)
  script.setAttribute('data-category', giscusConfig.category)
  script.setAttribute('data-category-id', giscusConfig.categoryId)
  script.setAttribute('data-mapping', giscusConfig.mapping)
  script.setAttribute('data-strict', giscusConfig.strict)
  script.setAttribute('data-reactions-enabled', giscusConfig.reactionsEnabled)
  script.setAttribute('data-emit-metadata', giscusConfig.emitMetadata)
  script.setAttribute('data-input-position', giscusConfig.inputPosition)
  script.setAttribute('data-theme', giscusConfig.theme)
  script.setAttribute('data-lang', giscusConfig.lang)
  script.setAttribute('crossorigin', 'anonymous')
  script.async = true
  container.value.appendChild(script)
})
</script>

<template>
  <div class="giscus-wrapper">
    <div v-if="!giscusConfig.categoryId" class="giscus-placeholder">
      <p>评论区未配置：请在 <code>docs/.vitepress/theme/giscus.config.ts</code> 中填入 <code>categoryId</code></p>
      <p><a href="https://giscus.app/zh-CN" target="_blank" rel="noopener">前往 giscus.app 获取</a></p>
    </div>
    <div ref="container" class="giscus-container"></div>
  </div>
</template>

<style scoped>
.giscus-wrapper {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid var(--vp-c-divider);
}

.giscus-placeholder {
  padding: 1.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.giscus-placeholder code {
  padding: 0.2em 0.4em;
  background: var(--vp-c-bg-mute);
  border-radius: 4px;
  font-size: 0.9em;
}

.giscus-placeholder a {
  color: var(--vp-c-brand-1);
}
</style>
