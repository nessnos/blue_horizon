<template>
    <div class="h-40 w-full">
        <table>
            <thead>
                <tr class="border-b border-gray-200 text-center text-xs">
                    <th v-for="(header, index) in headers" :key="index"
                    :title="header"
                        class="py-2 px-4 max-w-32 w-32 whitespace-nowrap overflow-hidden text-ellipsis">
                        {{ header }}
                    </th>
                </tr>
            </thead>
            <tbody class="h-32 overflow-y-auto">
                <tr v-for="(determinand, index) in paginatedDeterminands" :key="index" class="text-center text-xs">
                    <td v-for="(value, key) in determinand" :key="key" class="p-1">
                        <div :class="[key == 'uom' ? 'w-40 max-w-40' : 'max-w-32 w-32']"
                            class="whitespace-nowrap overflow-hidden text-ellipsis">
                            {{ formatValue(value) }}
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Pagination -->
    <div v-if="totalPages > 1" class="flex items-center justify-center gap-4">
        <div :disabled="currentPage === 1" class="text-ocen text-xs font-semibold" @click="prevPage">
            <ChevronLeftIcon class="h-4 w-4 text-gray-500 hover:cursor-pointer hover:text-ocean" />
        </div>
        <div class="text-xs">Page {{ currentPage }} of {{ totalPages }}</div>
        <div :disabled="currentPage === totalPages" class="text-ocen text-xs font-semibold" @click="nextPage">
            <ChevronRightIcon class="h-4 w-4 text-gray-500 hover:cursor-pointer hover:text-ocean" />
        </div>
    </div>
</template>
<script setup lang="ts">
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/24/outline"
import type * as types from "@/type"
import { computed, ref, watch } from "vue"

const props = defineProps<{
    headers: string[]
    labels?: string[]
    data?: { [key: string]: string | number }[]
}>()

const formatValue = (value: any) => {
    if (typeof value === "number") {
        if (value > 999999) {
            return value.toExponential(1);
        } else {
            return value.toLocaleString("fr-BE", { maximumFractionDigits: 2 });
        }
    }
    return value;
}
//TABLE PAGINATION SETUP
const itemsPerPage = 3;
const currentPage = ref(1);

const totalPages = computed(() =>
    Math.ceil((props.data?.length || 0) / itemsPerPage)
);

const paginatedDeterminands = computed(() => {
    if (!props.data) {
        return [];
    }

    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;

    return props.data.slice(start, end);
});


function nextPage() {
    if (currentPage.value < totalPages.value) {
        currentPage.value++;
    }
}

function prevPage() {
    if (currentPage.value > 1) {
        currentPage.value--;
    }
}

watch(
    () => props.data,
    (newData) => {
        currentPage.value = 1;
    },
    { immediate: true }
);
</script>
