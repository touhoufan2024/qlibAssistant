<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import { useRoute } from 'vitepress'
import SidebarToggle from './SidebarToggle.vue'

const { Layout } = DefaultTheme
const route = useRoute()
</script>

<template>
  <Layout>
    <template #nav-bar-title-after>
      <span @click.stop.prevent>
        <SidebarToggle />
      </span>
    </template>
  </Layout>
</template>
