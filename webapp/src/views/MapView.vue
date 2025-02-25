<template>
  <div class="flex h-screen">
    <SideBar class="border-none" />
    <div class="flex flex-grow justify-center">
      <Map />
    </div>
  </div>
</template>

<script lang="ts" setup>
import Map from "@/components/pages/MapPage.vue"
import SideBar from "@/components/share/SideBar.vue"
</script>