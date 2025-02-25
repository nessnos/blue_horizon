<template>
  <div class="flex h-screen">
    <SideBar class="border-none" />
    <div class="flex flex-grow justify-center">
      <HomePage />
    </div>
  </div>
</template>

<script lang="ts" setup>
import HomePage from "@/components/pages/HomePage.vue"
import SideBar from "@/components/share/SideBar.vue"
</script>
