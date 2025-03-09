<template>
<div class="group relative">
          <InformationCircleIcon class="h-4 w-4 cursor-pointer text-ocean" />

          <!-- Tooltip -->
          <div
            class="w-40 translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-black/80 px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
          >
            {{ text }}
          </div>
        </div>
</template>

<script setup lang="ts">
import {InformationCircleIcon} from "@heroicons/vue/24/outline";
import {defineProps} from "vue";

defineProps<{
  text: string
}>()
</script>