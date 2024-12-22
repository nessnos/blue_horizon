<template>
  <div class="font-nunito relative w-full h-full max-h-1/2">
    <!-- Background Image -->
    <div class="ocean-bg w-full h-full pt-4">
      <div class="mx-44">
        <div class="w-full h-full flex items-center justify-between p-3 py-4">
          <!-- Logo  -->
          <div class="flex flex-row gap-5 items-start">
            <img class="w-6 h-6" src="@/assets/logo/logo.png" alt="">
            <div class="font-bold text-lg text-ocean">Blue Horizon</div>
          </div>
          
          <!-- Map -->
          <div class="flex flex-row items-center gap-2 text-white bg-ocean hover:bg-gray-200 hover:text-ocean hover:cursor-pointer font-semibold rounded-lg shadow-lg p-2 px-4">
            <MapIcon class="h-5 w-5" />
            <span>Map</span>
          </div>
        </div>

        <div class="text-left text-ocean h-full w-1/2 mt-10">
          <div class="text-4xl font-extrabold">Welcome to Blue Horizon</div>
          <div class="text-lg pt-6">
            Discover detailed water quality metrics and statistics for Europe, 
            sourced from the European Environment Agency (EEA). Blue Horizon provides insights into water health across all European countries, 
            with data on key indicators. Our interactive map allows you to explore and compare water quality data for each country, 
            helping you understand the state of Europe’s water resources. 
          </div>
          <div class="pt-6 z-10">
            <div class="bg-ocean p-2 px-4 rounded-lg shadow-lg max-w-fit text-normal text-white hover:bg-gray-200 hover:text-ocean hover:cursor-pointer uppercase font-bold">
              Explore
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Wave Effect -->
    <div class="absolute bottom-0 left-0 right-0 w-full z-0">
      <svg viewBox="0 0 1440 320" xmlns="http://www.w3.org/2000/svg">
        <path
          fill="#ffffff"
          d="M0,180 C90,140 180,220 270,180 C360,140 450,220 540,180 C630,140 720,220 810,180 C900,140 990,220 1080,180 C1170,140 1260,220 1350,180 L1440,160 L1440,320 L0,320 Z"
          opacity="0.7"
        ></path>
        <path
          fill="#ffffff"
          d="M0,200 C80,180 160,220 240,200 C320,180 400,220 480,200 C560,180 640,220 720,200 C800,180 880,220 960,200 C1040,180 1120,220 1200,200 C1280,180 1360,220 1440,200 L1440,320 L0,320 Z"
          opacity="1"
        ></path>
      </svg>
    </div>
  </div>

  <div class="mx-44 my-24 mt-0">
    <div class="text-2xl font-extrabold text-ocean">
      Water Quality Metrics (Europe)
    </div>
    <div>
      Exploration Stats
    </div>
  </div>
</template>

<style>
.ocean-bg {
  background-image: url('@/assets/img/tap-water.jpg');
  background-position: center;
  background-size: cover;
}
</style>

<script setup lang="ts">
import { MapIcon } from "@heroicons/vue/24/outline";
</script>
