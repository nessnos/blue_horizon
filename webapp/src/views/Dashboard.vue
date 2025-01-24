<script setup lang="ts">
import { ref } from 'vue'
import type { Option } from "@/type";
import SelectOption from "@/assets/reusable/SelectOption.vue"

const countries = ref<Option[]>([
  { name: "Albania", isoAlpha2: "AL" },
  { name: "Andorra", isoAlpha2: "AD" },
  { name: "Armenia", isoAlpha2: "AM" },
  { name: "Austria", isoAlpha2: "AT" },
  { name: "Azerbaijan", isoAlpha2: "AZ" },
  { name: "Belarus", isoAlpha2: "BY" },
  { name: "Belgium", isoAlpha2: "BE" },
  { name: "Bosnia and Herzegovina", isoAlpha2: "BA" },
  { name: "Bulgaria", isoAlpha2: "BG" },
  { name: "Croatia", isoAlpha2: "HR" },
  { name: "Cyprus", isoAlpha2: "CY" },
  { name: "Czech Republic", isoAlpha2: "CZ" },
  { name: "Denmark", isoAlpha2: "DK" },
  { name: "Estonia", isoAlpha2: "EE" },
  { name: "Finland", isoAlpha2: "FI" },
  { name: "France", isoAlpha2: "FR" },
  { name: "Georgia", isoAlpha2: "GE" },
  { name: "Germany", isoAlpha2: "DE" },
  { name: "Greece", isoAlpha2: "GR" },
  { name: "Hungary", isoAlpha2: "HU" },
  { name: "Iceland", isoAlpha2: "IS" },
  { name: "Ireland", isoAlpha2: "IE" },
  { name: "Italy", isoAlpha2: "IT" },
  { name: "Kazakhstan", isoAlpha2: "KZ" },
  { name: "Kosovo", isoAlpha2: "XK" },
  { name: "Latvia", isoAlpha2: "LV" },
  { name: "Liechtenstein", isoAlpha2: "LI" },
  { name: "Lithuania", isoAlpha2: "LT" },
  { name: "Luxembourg", isoAlpha2: "LU" },
  { name: "Malta", isoAlpha2: "MT" },
  { name: "Moldova", isoAlpha2: "MD" },
  { name: "Monaco", isoAlpha2: "MC" },
  { name: "Montenegro", isoAlpha2: "ME" },
  { name: "Netherlands", isoAlpha2: "NL" },
  { name: "North Macedonia", isoAlpha2: "MK" },
  { name: "Norway", isoAlpha2: "NO" },
  { name: "Poland", isoAlpha2: "PL" },
  { name: "Portugal", isoAlpha2: "PT" },
  { name: "Romania", isoAlpha2: "RO" },
  { name: "Russia", isoAlpha2: "RU" },
  { name: "San Marino", isoAlpha2: "SM" },
  { name: "Serbia", isoAlpha2: "RS" },
  { name: "Slovakia", isoAlpha2: "SK" },
  { name: "Slovenia", isoAlpha2: "SI" },
  { name: "Spain", isoAlpha2: "ES" },
  { name: "Sweden", isoAlpha2: "SE" },
  { name: "Switzerland", isoAlpha2: "CH" },
  { name: "Turkey", isoAlpha2: "TR" },
  { name: "Ukraine", isoAlpha2: "UA" },
  { name: "United Kingdom", isoAlpha2: "GB" },
  { name: "Vatican City", isoAlpha2: "VA" },
]);

const decades = ref<{ name: string }[]>([
  { name: '1900-1910' },
  { name: '1910-1920' },
  { name: '1920-1930' },
  { name: '1930-1940' },
  { name: '1940-1950' },
  { name: '1950-1960' },
  { name: '1960-1970' },
  { name: '1970-1980' },
  { name: '1980-1990' },
  { name: '1990-2000' },
  { name: '2000-2010' },
  { name: '2010-2020' },
  { name: '2020-2030' },
]);

const chemicals = ref<Option[]>([
  { name: "Tetrachloroethylene", code: "CAS_127-18-4" },
  { name: "Trichloroethylene", code: "CAS_79-01-6" },
  { name: "Perchloroethylene", code: "CAS_127-18-4" },
  { name: "Chloroform", code: "CAS_67-66-3" },
  { name: "Dichloromethane", code: "CAS_75-09-2" },
  { name: "Carbon Tetrachloride", code: "CAS_56-23-5" },
  { name: "1,1,1-Trichloroethane", code: "CAS_71-55-6" },
  { name: "Methylene Chloride", code: "CAS_75-09-2" },
  { name: "Tetrachloromethane", code: "CAS_56-23-5" },
  { name: "Bromotrichloromethane", code: "CAS_75-64-9" },
  { name: "Perfluorocyclopropane", code: "CAS_675-99-2" },
  { name: "Hexachloroethane", code: "CAS_67-72-1" }
]);


</script>
<template>
    <div class="p-12">
        <div class="flex flex-row gap-3">
            <SelectOption
                :rowData="countries"
                :label="'Country'"
            />
            <SelectOption
                :rowData="decades"
                :label="'Decades'"
            />
            <SelectOption
                :rowData="chemicals"
                :label="'Chemicals'"
            />
        </div>
    </div>
</template>