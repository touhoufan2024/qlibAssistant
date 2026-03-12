<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import { useRoute } from 'vitepress'
import SidebarToggle from './SidebarToggle.vue'
import Giscus from './Giscus.vue'

const { Layout } = DefaultTheme
const route = useRoute()
</script>

<template>
  <Layout>
    <template #nav-bar-title-after>
      <SidebarToggle />
    </template>
    <template #doc-after>
      <Giscus :key="route.path" />
    </template>
  </Layout>
</template>
