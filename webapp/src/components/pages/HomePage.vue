<template>
  <div class="flex flex-col gap-6 p-12">
    <div class="text-3xl font-bold text-ocean">Welcome to Blue Horizon</div>
    <div class="w-2/3 text-ocean">
      Dive into detailed water quality metrics and statistics for Europe,
      sourced from the European Environment Agency (EEA). Gain insights into key
      indicators of water health across all European countries, presented in a
      user-friendly interface.
    </div>
    <div class="text-xl font-semibold text-ocean">Try out</div>
    <div class="flex flex-row gap-6 px-3">
      <div
        class="flex h-fit min-h-64 min-w-56 flex-col items-start justify-between gap-2 rounded-lg border-[0.5px] border-gray-300 bg-gray-100/55 px-6 py-4 shadow"
      >
        <div class="relative h-full w-56 p-1 py-4">
          <img alt="" class="rounded" src="../../assets/img/statistics.png" />
          <div class="absolute bottom-0 h-12 w-full bg-gray-100 blur-lg"></div>
          <!-- Blur effect -->
        </div>
        <div class="max-w-56 py-3">
          <div class="text-sm font-normal">Statistics Dashboard</div>
          <div class="py-2 text-xs">
            Access a dashboard with water quality metrics like pH, pollution,
            and availability. Filter by country or year to track trends and
            explore changes in water health over time.
          </div>
        </div>
        <RouterLink
          :to="'/dashboard'"
          class="rounded-lg bg-ocean px-3 py-2 text-sm text-white hover:cursor-pointer hover:bg-aqua"
          >Learn More
        </RouterLink>
      </div>
      <div
        class="flex h-fit min-h-64 min-w-56 flex-col items-start justify-between gap-2 rounded-lg border-[0.5px] border-gray-300 bg-gray-100/55 px-6 py-4 shadow"
      >
        <div class="relative h-full w-56 p-1 py-4">
          <img alt="" class="rounded" src="../../assets/img/map.png" />
          <div class="absolute bottom-0 h-12 w-full bg-gray-100 blur-lg"></div>
          <!-- Blur effect -->
        </div>
        <div class="max-w-56 py-3">
          <div class="text-sm font-normal">Interactive Map</div>
          <div class="py-2 text-xs">
            Explore Europe’s water quality through an interactive map. Select
            countries to view detailed metrics, offering localized insights into
            water health and key statistics.
          </div>
        </div>
        <RouterLink
          :to="'/map'"
          class="rounded-lg bg-ocean px-3 py-2 text-sm text-white hover:cursor-pointer hover:bg-aqua"
          >Learn More
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { RouterLink } from "vue-router"
</script>