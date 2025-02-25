<template>
  <div class="flex flex-row">
    <div
      class="absolute inline-flex h-screen transform flex-col items-center bg-ocean p-2 px-3 shadow transition-all duration-300 ease-in-out md:relative md:left-0"
    >
      <nav class="mt-6 inline-flex flex-col space-y-2">
        <SideBarButton
          to="/"
          :icon="HomeIcon"
          :label="'Home'"
          :isActive="isActive('/')"
        />
        <SideBarButton
          to="/dashboard"
          :icon="ChartPieIcon"
          :label="'Dashboard'"
          :isActive="isActive('/dashboard')"
        />
        <SideBarButton
          to="/map"
          :icon="MapIcon"
          :label="'Map'"
          :isActive="isActive('/map')"
        />
      </nav>
    </div>
    <div class="max-h-screen w-full bg-ocean/10">
      <RouterView />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { RouterView, useRoute } from "vue-router"
import { ChartPieIcon, HomeIcon, MapIcon } from "@heroicons/vue/24/solid"
import SideBarButton from "@/components/templates/SideBarButton.vue"

const isActive = (path: string) => {
  const route = useRoute()
  return route.path === path
}
</script>