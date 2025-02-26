<template>
  <div class="flex flex-col gap-6 p-12">
    <div class="flex text-3xl text-ocean gap-2">
      <div>Welcome to</div>
      <div class="font-bold">Blue Horizon</div>
    </div>
    <div class="w-2/3 text-ocean">
      Dive into detailed water quality metrics and statistics for Europe,
      sourced from the European Environment Agency (EEA). Gain insights into key
      indicators of water health across all European countries, presented in a
      user-friendly interface.
    </div>
    <div class="text-xl font-semibold text-ocean">Try out</div>
    <div class="flex flex-row gap-6 px-3">
      <HomeInformationCard
        title="Statistics Dashboard"
        description="Access a dashboard with water quality metrics like pH, pollution, and availability. Filter by country or year to track trends and explore changes in water health over time."
        :icon="BarGraph"
        link="/dashboard"
      />
      <HomeInformationCard
        title="Interactive Map"
        description="Explore Europe’s water quality through an interactive map. Select countries to view detailed metrics, offering localized insights into water health and key statistics."
        :icon="MapPin"
        link="/map"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import HomeInformationCard from '@/components/reusable/cards/HomeInformationCard.vue'
import BarGraph from "@/assets/icons/BarGraph.vue"
import MapPin from "@/assets/icons/MapPin.vue";
</script>