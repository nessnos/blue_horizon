<template>
  <div class="flex">
    <div class="relative left-0 h-screen bg-ocean px-3 pb-2 shadow">
      <nav class="mt-6 flex flex-col items-center space-y-2">
        <RouterLink to="/" class="mb-2 w-10">
          <img
            alt="Blue Horizon"
            src="@/assets/images/Blue%20Horizon%20Logo%20White.png"
          />
        </RouterLink>

        <SideBarButton
          :icon="HomeIcon"
          :isActive="isActive('/')"
          :label="'Page d\'Accueil'"
          to="/"
        />
        <SideBarButton
          :icon="ChartPieIcon"
          :isActive="isActive('/dashboard')"
          :label="'Interface de statistiques'"
          to="/dashboard"
        />
        <SideBarButton
          :icon="MapIcon"
          :isActive="isActive('/map')"
          :label="'Carte Interactive'"
          to="/map"
        />
        <SideBarButton
          :icon="WrenchScrewdriverIcon"
          :isActive="isActive('/machine-learning')"
          :label="'Machine Learning'"
          to="/machine-learning"
        />
        <SideBarButton
          :demo="true"
          :icon="ChatBubbleBottomCenterTextIcon"
          :isActive="isActive('/chat')"
          :label="'Chat'"
          to="/chat"
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
import {
  ChartPieIcon,
  ChatBubbleBottomCenterTextIcon,
  HomeIcon,
  MapIcon,
  WrenchScrewdriverIcon,
} from "@heroicons/vue/24/solid"
import SideBarButton from "@/components/reusable/buttons/SideBarButton.vue"

const isActive = (path: string) => {
  const route = useRoute()
  return route.path === path
}
</script>
