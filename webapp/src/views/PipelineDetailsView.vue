<template>
  <div class="flex h-screen">
    <SideBar class="border-none" />
    <div class="flex flex-grow justify-center">
      <PipelineDetails />
    </div>
  </div>
</template>

<script lang="ts" setup>
import PipelineDetails from "@/components/pages/PipelineDetailsPage.vue"
import SideBar from "@/components/share/SideBar.vue"
</script>
