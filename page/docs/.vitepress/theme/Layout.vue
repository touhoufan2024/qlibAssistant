<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import SidebarToggle from './SidebarToggle.vue'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #nav-bar-title-after>
      <SidebarToggle />
    </template>
  </Layout>
</template>
