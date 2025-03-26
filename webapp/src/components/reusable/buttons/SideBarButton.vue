<template>
  <div class="group relative">
    <RouterLink
      :to="to"
      :class="[
        isActive ? 'bg-white' : '',
        'flex flex-row gap-4 rounded-lg p-3 text-white transition duration-200 ease-in-out',
        isActive
          ? ''
          : 'transition-all duration-200 ease-in-out hover:cursor-pointer hover:bg-blue-900',
      ]"
    >
      <component
        :is="icon"
        :class="['h-6 w-6', isActive ? 'text-ocean' : 'text-white']"
      />
      <div
        v-if="demo"
        :class="[isActive ? 'text-ocean' : 'text-white']"
        class="absolute bottom-[0.15rem] right-[0.2rem] rounded text-[0.43rem] font-semibold uppercase"
      >
        demo
      </div>
    </RouterLink>
    <div
      class="pointer-events-none absolute left-1/2 mt-1 w-fit -translate-y-10 translate-x-6 transform rounded-lg bg-black bg-opacity-80 px-2 py-1 text-center text-xs text-white opacity-0 transition-opacity duration-200 group-hover:opacity-100"
    >
      {{ label }}
    </div>
  </div>
</template>

<script lang="ts" setup>
const {
  to,
  icon,
  label,
  isActive,
  demo = false,
} = defineProps<{
  to: string
  icon: any
  label: string
  isActive: boolean
  demo?: boolean
}>()
</script>
