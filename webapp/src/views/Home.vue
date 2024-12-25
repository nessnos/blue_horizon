<template>
  <div class="font-nunito relative w-full h-screen">
    <!-- Background Image with Overlay -->
    <div class="ocean-bg w-full h-full relative">
      <!-- Overlay -->
      <div class="absolute inset-0 bg-black bg-opacity-35 z-10"></div>

      <div class="relative z-20 mx-44">
        <div class="w-full h-full flex items-center justify-between p-3 py-4">
          <!-- Logo -->
          <div class="flex flex-row gap-3 items-end p-2 px-4 rounded-lg">
            <div class="font-bold text-2xl text-white">Blue Horizon</div>
          </div>

          <!-- Map -->
          <div class="flex flex-row items-center gap-2 text-white bg-ocean hover:bg-gray-200 hover:text-ocean hover:cursor-pointer font-semibold rounded-lg shadow-lg p-2 px-4">
            <MapIcon class="h-5 w-5" />
            <span>Map</span>
          </div>
        </div>

        <div class="mt-32 px-24 text-center text-white h-full w-full flex flex-col gap-12 items-center justify-center gap-12">
          <div class="text-4xl font-extrabold">Understanding Europe’s Water Quality</div>
          <div class="text-lg font-semibold">
            Discover detailed water quality metrics and statistics for Europe, sourced from the European Environment Agency (EEA). 
            Blue Horizon provides insights into water health across all European countries, with data on key indicators. Our interactive 
            map allows you to explore and compare water quality data for each country, helping you understand the state of Europe’s water 
            resources.
          </div>
          <div class="w-full flex flex-row justify-center">
            <div class="bg-ocean p-2 px-4 w-fit rounded-lg shadow-lg text-normal text-white hover:bg-gray-200 hover:text-ocean hover:cursor-pointer uppercase font-bold">
              Explore
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="px-44 py-12 w-full">
    <div class="font-bold text-2xl text-center py-4 text-ocean">Analyze Water Quality Metrics</div>
    <div class="text-normal text-center text-ocean py-4 pb-12">
      Access comprehensive water quality data across Europe, sourced from the European Environment Agency (EEA). 
      With customizable filters, you can view metrics for all of Europe or focus on specific countries for localized insights. 
      Use the year filter to track changes over time and analyze key indicators such as pH levels, pollution rates, and water availability. 
      This section allows you to explore detailed statistics to better understand the state of water resources across the continent.
    </div>
    <div class="bg-ocean rounded-full shadow h-fit min-h-16 flex flex-row gap-12 items-center px-12 p-2">
      <div class="bg-white text-ocean font-semibold px-3 p-1 rounded-lg">Country</div>
      <div class="bg-white text-ocean font-semibold px-3 p-1 rounded-lg">Year</div>
    </div>
    <div>Cards</div>
  </div>
</template>

<style>
.ocean-bg {
  background-image: url('@/assets/img/drops.jpeg');
  background-position: center;
  background-size: cover;
}
</style>

<script setup lang="ts">
import { MapIcon } from "@heroicons/vue/24/outline";
</script>
