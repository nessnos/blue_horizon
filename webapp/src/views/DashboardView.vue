<template>
  <div class="flex h-screen">
    <SideBar class="border-none" />
    <div class="flex flex-grow justify-center overflow-scroll">
      <Dashboard />
    </div>
  </div>
</template>

<script lang="ts" setup>
import Dashboard from "@/components/pages/DashboardPage.vue"
import SideBar from "@/components/share/SideBar.vue"
</script>
