<template>
  <div class="flex">
    <div
      class="h-screen bg-ocean pb-2 px-3 shadow relative left-0"
    >
      <nav class="mt-6 flex flex-col space-y-2 items-center">
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
import { ChartPieIcon, HomeIcon, MapIcon, WrenchScrewdriverIcon, ChatBubbleBottomCenterTextIcon } from "@heroicons/vue/24/solid"
import SideBarButton from "@/components/reusable/buttons/SideBarButton.vue"

const isActive = (path: string) => {
  const route = useRoute()
  return route.path === path
}
</script>