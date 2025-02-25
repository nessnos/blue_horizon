<script lang="ts" setup>
import { ref } from "vue"
import { RouterLink, RouterView, useRoute } from "vue-router"
import { ChartPieIcon, HomeIcon, MapIcon } from "@heroicons/vue/24/outline"

const isOpen = ref(false)

const openSidebar = () => {
  console.log(isOpen.value)
  return (isOpen.value = !isOpen.value)
}

const isActive = (path: string) => {
  const route = useRoute()
  return route.path === path
}
</script>
<template>
  <div class="flex flex-row">
    <div
      :class="[[isOpen ? 'w-72' : '']]"
      class="absolute inline-flex h-screen transform flex-col items-center bg-ocean p-2 px-3 shadow transition transition-all duration-200 duration-300 ease-in-out md:relative md:left-0"
    >
      <div class="my-6 flex w-full items-end justify-between px-4">
        <div v-if="isOpen" class="text-xl font-bold text-white">
          Blue Horizon
        </div>
        <!--≈<div @click="openSidebar"  class="p-2 rounded-full text-center text-white bg-gray-500/55">
          <ChevronLeftIcon v-if="isOpen" class="h-4 w-4" />
          <ChevronRightIcon v-if="!isOpen" class="h-4 w-4" />
        </div>-->
      </div>
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
