
<script setup lang="ts">
</script>

<template>
  <div class="flex flex-col gap-6 p-12">
    <div class="text-3xl font-bold text-ocean">Welcome to Blue Horizon</div>
    <div class="text-ocean">
      Discover detailed water quality metrics and statistics for Europe, sourced from the European Environment Agency (EEA). 
      Blue Horizon provides insights into water health across all European countries, with data on key indicators. Our interactive 
      map allows you to explore and compare water quality data for each country, helping you understand the state of Europe’s water 
      resources.
    </div>
    <div class="font-semibold text-xl text-ocean">Try out</div>
    <div class="flex flex-row gap-6 px-3">
      <div class="flex flex-col gap-2 items-start justify-between border-[0.5px] border-gray-300 rounded-lg bg-gray-100/55 shadow px-6 py-4 h-fit min-h-64 min-w-56">
        <div class="relative w-56 h-full p-1 py-4">
          <img class="rounded" src='@/assets/img/statistics.png' alt="">
          <div class="absolute bottom-0 w-full h-14 blur-lg bg-gray-100"></div><!-- Blur effect -->
        </div>
        <div class="py-3">
          <div class="text-sm font-normal">Stastical Anaylsis</div>
          <div class="text-xs py-2">jsjqdkjksdef</div>
        </div>
        <div class="bg-ocean rounded-lg px-3 py-2 text-white text-sm hover:bg-aqua hover:cursor-pointer">Learn More</div>
      </div>
      <div class="flex flex-col gap-2 items-start justify-between border-[0.5px] border-gray-400 rounded-lg bg-white shadow px-6 py-4 h-64 min-w-56">
        <div class="text-sm">Interactive Map</div>
        <div class="bg-ocean rounded-lg px-3 py-2 text-white text-sm hover:bg-aqua hover:cursor-pointer">Learn More</div>
      </div>
    </div>
  </div>
          
</template>



