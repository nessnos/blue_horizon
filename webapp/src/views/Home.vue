
<script setup lang="ts">
import { RouterLink } from 'vue-router';

</script>

<template>
  <div class="flex flex-col gap-6 p-12">
    <div class="text-3xl font-bold text-ocean">Welcome to Blue Horizon</div>
    <div class="text-ocean w-2/3">
      Dive into detailed water quality metrics and statistics for Europe, sourced from the European Environment Agency (EEA). 
      Gain insights into key indicators of water health across all European countries, presented in a user-friendly interface.
    </div>
    <div class="font-semibold text-xl text-ocean">Try out</div>
    <div class="flex flex-row gap-6 px-3">
      <div class="flex flex-col gap-2 items-start justify-between border-[0.5px] border-gray-300 rounded-lg bg-gray-100/55 shadow px-6 py-4 h-fit min-h-64 min-w-56">
        <div class="relative w-56 h-full p-1 py-4">
          <img class="rounded" src='@/assets/img/statistics.png' alt="">
          <div class="absolute bottom-0 w-full h-12 blur-lg bg-gray-100"></div><!-- Blur effect -->
        </div>
        <div class="py-3 max-w-56">
          <div class="text-sm font-normal">Statistics Dashboard</div>
          <div class="text-xs py-2">
            Access a dashboard with water quality metrics like pH, pollution, and availability. 
            Filter by country or year to track trends and explore changes in water health over time.
          </div>
        </div>
        <RouterLink :to="'/dashboard'" class="bg-ocean rounded-lg px-3 py-2 text-white text-sm hover:bg-aqua hover:cursor-pointer">Learn More</RouterLink>
      </div>
      <div class="flex flex-col gap-2 items-start justify-between border-[0.5px] border-gray-300 rounded-lg bg-gray-100/55 shadow px-6 py-4 h-fit min-h-64 min-w-56">
        <div class="relative w-56 h-full p-1 py-4">
          <img class="rounded" src='@/assets/img/map.png' alt="">
          <div class="absolute bottom-0 w-full h-12 blur-lg bg-gray-100"></div><!-- Blur effect -->
        </div>
        <div class="py-3 max-w-56">
          <div class="text-sm font-normal">Interactive Map</div>
          <div class="text-xs py-2">
            Explore Europe’s water quality through an interactive map. 
            Select countries to view detailed metrics, offering localized insights into water health and key statistics.
          </div>
        </div>
        <RouterLink :to="'/map'" class="bg-ocean rounded-lg px-3 py-2 text-white text-sm hover:bg-aqua hover:cursor-pointer">Learn More</RouterLink>
      </div>
    </div>
  </div>
          
</template>



