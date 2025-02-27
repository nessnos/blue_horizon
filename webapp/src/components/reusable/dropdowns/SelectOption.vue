<template>
  <div class="w-72">
    <span class="mb-3 pl-1 text-sm font-semibold text-ocean">{{ label }}</span>
    <Listbox v-model="selectedData">
      <div class="relative mt-1">
        <ListboxButton
          class="relative w-full cursor-default rounded-lg border border-ocean/50 py-2 pl-3 pr-10 text-left text-sm"
        >
          <span v-if="selectedData" class="block truncate">{{
            selectedData.name
          }}</span>
        </ListboxButton>

        <transition
          leave-active-class="transition duration-100 ease-in"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <ListboxOptions
            class="absolute z-10 mt-1 max-h-60 w-full overflow-auto bg-white border border-ocean/50 rounded-lg py-1 text-sm shadow-md"
          >
            <ListboxOption
              v-for="data in rowData"
              :key="data.name"
              v-slot="{ active, selected }"
              :value="data"
              as="template"
            >
              <li
                :class="[
                  active ? 'bg-ocean text-white' : 'text-gray-900',
                  'relative cursor-default select-none py-2 pl-4 pr-4',
                ]"
              >
                <span
                  :class="[
                    selected ? 'font-medium' : 'font-normal',
                    'block truncate',
                  ]"
                  >{{ data.name }}</span
                >
                <span
                  v-if="selected"
                  class="absolute inset-y-0 left-0 flex items-center pl-3 text-amber-600"
                >
                </span>
              </li>
            </ListboxOption>
          </ListboxOptions>
        </transition>
      </div>
    </Listbox>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from "vue"
import {
  Listbox,
  ListboxButton,
  ListboxOption,
  ListboxOptions,
} from "@headlessui/vue"
import type { Option } from "@/type"

const props = defineProps<{
  rowData: Option[]
  label: String
  default: Option
}>()
const selectedData = ref(props.rowData[0])

onMounted(() => {
  selectedData.value = props.default
})
</script>
