<template>
  <div class="w-72">
    <span class="mb-3 pl-1 text-sm font-semibold text-ocean">{{ label }}</span>
    <Listbox v-model="selectedData">
      <div class="relative mt-1">
        <ListboxButton
          class="relative w-full cursor-default rounded-lg border border-ocean/50 py-2 pl-3 pr-10 text-left text-sm">
          <div class="flex flex-row gap-3 items-center" v-if="selectedData">
            <span v-if="flag && selectedData.name != 'Tout'" class="fi rounded-[0.2rem] shadow"
              :class="'fi-' + selectedData.code?.toLowerCase()"></span>
            <span class="block truncate">{{ selectedData.name }}</span>
          </div>
        </ListboxButton>

        <transition leave-active-class="transition duration-100 ease-in" leave-from-class="opacity-100"
          leave-to-class="opacity-0">
          <ListboxOptions
            class="absolute z-10 mt-1 max-h-60 w-full overflow-auto bg-white border border-ocean/50 rounded-lg py-1 text-sm shadow-md">
            <ListboxOption @click='handleSelectChange' v-for="data in rowData" :key="data.name"
              v-slot="{ active, selected }" :value="data" as="template">
              <li :class="[
                active ? 'bg-ocean text-white transition-all duration-200 ease-in-out' : 'text-gray-900',
                'relative cursor-default select-none py-2 pl-4 pr-4',
              ]">
                <div class="flex flex-row gap-3 items-center">
                  <span v-if="flag && data.name != 'Tout'" class="fi rounded-[0.2rem] shadow"
                    :class="'fi-' + data.code?.toLowerCase()"></span>
                  <span :class="[
                    selected ? 'font-medium' : 'font-normal',
                    'block truncate',
                  ]">{{ data.name }}</span>
                </div>
              </li>
            </ListboxOption>
          </ListboxOptions>
        </transition>
      </div>
    </Listbox>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch } from "vue"
import {
  Listbox,
  ListboxButton,
  ListboxOption,
  ListboxOptions,
} from "@headlessui/vue"
import type * as types from "@/type"

const props = defineProps<{
  rowData: types.Option[]
  label: String
  default: types.Option,
  flag?: boolean,
}>()


const selectedData = ref(props.rowData[0])

const emit = defineEmits(['update:selectedData']);

const handleSelectChange = () => {
  emit('update:selectedData', selectedData.value);
};

onMounted(() => {
  selectedData.value = props.default
})

watch(
  () => props.default,
  (newDefault) => {
    if (props.rowData.some((item) => item.name === newDefault.name)) {
      selectedData.value = newDefault;
    }
  },
  { immediate: true }
);
</script>
