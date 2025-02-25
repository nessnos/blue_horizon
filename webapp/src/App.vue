<template>
  <div class="flex flex-row">
    <div
      class="absolute inline-flex h-screen transform flex-col items-center bg-ocean p-2 px-3 shadow transition-all duration-300 ease-in-out md:relative md:left-0"
    >
      <nav
        class="mt-6 inline-flex flex-col space-y-2"
        v-bind:class="{ 'w-full': isOpen }"
      >
        <RouterLink
          :class="[isActive('/') ? 'bg-aqua' : '', '']"
          class="flex flex-row gap-4 rounded-lg p-3 text-white hover:cursor-pointer"
          to="/"
        >
          <HomeIcon class="h-6 w-6" />
          <div v-if="isOpen" class="font-semibold">Home</div>
        </RouterLink>
        <RouterLink
          :class="[isActive('/dashboard') ? 'bg-aqua' : '', '']"
          class="flex flex-row gap-4 rounded-lg p-3 text-white hover:cursor-pointer hover:bg-aqua"
          to="/dashboard"
        >
          <ChartPieIcon class="h-6 w-6" />
          <div v-if="isOpen" class="font-semibold">Dashboard</div>
        </RouterLink>
        <RouterLink
          :class="[isActive('/map') ? 'bg-aqua' : '', '']"
          class="flex flex-row gap-4 rounded-lg p-3 text-white hover:cursor-pointer hover:bg-aqua"
          to="/map"
        >
          <MapIcon class="h-6 w-6" />
          <div v-if="isOpen" class="font-semibold">Map</div>
        </RouterLink>
      </nav>
    </div>
    <div class="max-h-screen w-full bg-ocean/10">
      <RouterView />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { RouterLink, RouterView, useRoute } from "vue-router"
import { ChartPieIcon, HomeIcon, MapIcon } from "@heroicons/vue/24/outline"

const isActive = (path: string) => {
  const route = useRoute()
  return route.path === path
}
</script>
