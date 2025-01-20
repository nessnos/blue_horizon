<script setup lang="ts">
import { ref } from "vue"
import { RouterView, RouterLink, useRoute, useRouter } from "vue-router"
import { ChevronRightIcon, ChevronLeftIcon, HomeIcon, ChartPieIcon, MapIcon } from "@heroicons/vue/24/outline";

const isOpen = ref(false)

const openSidebar = () => {
  console.log(isOpen.value)
  return isOpen.value = !isOpen.value
}

const isActive = (path: string) => {
  const route = useRoute();
  return route.path === path;
};

</script>
<template>
 <div class="flex flex-row">
  <div class="transition-all duration-300 absolute h-screen inline-flex flex-col items-center bg-ocean shadow p-2 px-3 transform md:relative md:left-0 transition duration-200 ease-in-out" 
  :class="[ 
                 [ isOpen ? 'w-72' : '' ]
      ]">
    <div class="my-6 w-full px-4 flex justify-between items-end">
      <div v-if="isOpen" class="font-bold text-white text-xl">Blue Horizon</div>
      <!--≈<div @click="openSidebar"  class="p-2 rounded-full text-center text-white bg-gray-500/55">
        <ChevronLeftIcon v-if="isOpen" class="h-4 w-4" />
        <ChevronRightIcon v-if="!isOpen" class="h-4 w-4" />
      </div>-->
    </div>
    <nav class="inline-flex flex-col space-y-2 mt-6" v-bind:class="{ 'w-full': isOpen }">
      <RouterLink to="/" class="flex flex-row gap-4 text-white p-3 rounded-lg hover:cursor-pointer"
        :class="[isActive('/') ? 'bg-aqua' : '', '']"
      >
        <HomeIcon class="h-6 w-6" />
        <div v-if="isOpen" class="font-semibold">Home</div>
      </RouterLink>
      <RouterLink to="/dashboard" class="flex flex-row gap-4 text-white p-3 rounded-lg hover:bg-aqua hover:cursor-pointer"
        :class="[isActive('/dashboard') ? 'bg-aqua' : '', '']"
      >
        <ChartPieIcon class="h-6 w-6" />
        <div v-if="isOpen" class="font-semibold">Dashboard</div>
      </RouterLink>
      <RouterLink to="/map" class="flex flex-row gap-4 text-white p-3 rounded-lg hover:bg-aqua hover:cursor-pointer"
        :class="[isActive('/map') ? 'bg-aqua' : '', '']"
      >
        <MapIcon class="h-6 w-6" />
        <div v-if="isOpen" class="font-semibold">Map</div>
      </RouterLink>
    </nav>
  </div>
  <div class="w-full bg-white max-h-screen">
    <RouterView/>
  </div>
 </div>
</template>

