<template>
  <div class="flex h-screen">
    <SideBar class="border-none" />
    <div class="flex flex-grow justify-center">
      <MachineLearning />
    </div>
  </div>
</template>

<script lang="ts" setup>
import MachineLearning from "@/components/pages/MachineLearningPage.vue"
import SideBar from "@/components/share/SideBar.vue"
</script>
