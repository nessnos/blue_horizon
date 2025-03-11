<template>
  <div class="flex flex-col gap-6 p-12">
    <div class="flex gap-2 text-4xl text-ocean">
      <div>Welcome to</div>
      <div class="flex">
        <div class="font-bold">BLUE H</div>
        <div class="mb-2 w-10">
          <img alt="Blue Horizon" src="@/assets/images/Blue%20Horizon%20Logo.png" />
        </div>
        <div class="font-bold">RIZON</div>
      </div>
    </div>
    <div class="w-2/3 text-ocean">
      Explorez dans des données détaillées sur la qualité de l'eau et les statistiques pour l'Europe, fournies par
      l'Agence Européenne de l'Environnement (AEE). Découvrez les indicateurs clés de la santé de l'eau à travers les
      pays européens, dans une interface facile à utiliser.
    </div>
    <div class="text-xl font-semibold text-ocean">Testez</div>
    <div class="flex flex-row gap-6 px-3">
      <HomeInformationCard :icon="ChartPieIcon"
        description="Accédez à un interface de statistiques interactif affichant des métriques de qualité de l'eau. 
                      Appliquez des filtres par pays ou année pour observer les tendances et les changements dans la santé de l'eau au fil du temps."
        link="/dashboard" title="Interface de statistiques" />
      <HomeInformationCard :icon="MapIcon" description="Explorez la qualité de l'eau en Europe à travers une carte interactive. Sélectionnez les pays pour consulter des métriques détaillées, 
                      offrant des aperçus localisés sur la santé de l'eau et des statistiques clés." link="/map"
        title="Carte Interactive" />
      <HomeInformationCard :icon="WrenchScrewdriverIcon" description="Lancez des pipelines pour exécuter des modèles de prédiction comme la régression linéaire.
                    Obtenez des prévisions précises basées sur vos données et suivez l'évolution de vos modèles."
        link="/machine-learning" title="Machine Learning" />
      <HomeInformationCard :icon="ChatBubbleBottomCenterTextIcon" :demo=true
        description="Interagissez avec notre chatbot pour analyser et explorer en profondeur les indicateurs de qualité de l'eau. 
                                                                Posez vos questions et obtenez des réponses claires et détaillées !" link="/chat"
        title="Explorez l'IA" />
    </div>
  </div>
</template>

<script lang="ts" setup>
  import HomeInformationCard from "@/components/reusable/cards/HomeInformationCard.vue"
  import { ChartPieIcon, MapIcon, WrenchScrewdriverIcon, ChatBubbleBottomCenterTextIcon } from "@heroicons/vue/24/solid"
</script>