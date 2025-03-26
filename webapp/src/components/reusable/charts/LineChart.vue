<template>
  <div id="line-chart" class="px-2 pt-4"></div>
</template>
<script lang="ts" setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue"
import ApexCharts from "apexcharts"
import type * as types from "@/type"

const props = defineProps<{
  data: types.ChartData[] | undefined
}>()

const chartInstance = ref<ApexCharts | null>(null)

const renderChart = () => {
  if (chartInstance.value) {
    chartInstance.value.destroy()
  }

  const options = {
    series: [
      {
        name: "Moyenne Chemicals",
        data: props.data,
      },
    ],
    chart: {
      height: "100%",
      type: "line",
      toolbar: {
        show: false,
      },
      zoom: {
        enabled: false,
        allowMouseWheelZoom: false,
      },
    },
    stroke: {
      width: 3,
      curve: "smooth",
    },
    xaxis: {
      type: "category",
      tickAmount: 11,
      labels: {
        show: true,
        rotate: 0,
        rotateAlways: false,
        hideOverlappingLabels: false,
        style: {
          colors: "#D2D2D2",
        },
      },
      crosshairs: {
        width: 1,
        stroke: {
          color: "#1F51C1",
          dashArray: 0,
        },
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      labels: {
        formatter: function (value: number) {
          return value.toLocaleString("fr-BE", { maximumFractionDigits: 2 })
        },
      },
    },
    grid: {
      show: false,
    },
    markers: {
      size: 0,
      colors: "#002665",
      strokeColors: undefined,
      strokeWidth: 0,
      strokeOpacity: 0,
      strokeDashArray: 0,
      fillOpacity: 1,
      discrete: [],
      shape: "circle",
      offsetX: 0,
      offsetY: 0,
      onClick: undefined,
      onDblClick: undefined,
      showNullDataPoints: true,
      hover: {
        size: undefined,
        sizeOffset: 6,
      },
    },
    title: {
      text: "",
      align: "left",
      style: {
        fontSize: "12px",
        color: "#666",
      },
    },
    fill: {
      type: "solid",
      opacity: 1,
      colors: ["#002665"],
    },
    tooltip: {
      custom: function ({
        series,
        seriesIndex,
        dataPointIndex,
        w,
      }: {
        series: any[]
        seriesIndex: number
        dataPointIndex: number
        w: any
      }) {
        var data = w.globals.initialSeries[seriesIndex].data[dataPointIndex]

        return (
          '<div class="p-1.5 bg-black/80 text-white text-xs"> Moyenne : ' +
          data.y.toLocaleString("fr-BE", { maximumFractionDigits: 2 }) +
          "</div>"
        )
      },
    },
  }

  if (
    document.getElementById("line-chart") &&
    typeof ApexCharts !== "undefined"
  ) {
    chartInstance.value = new ApexCharts(
      document.getElementById("line-chart"),
      options
    )
    chartInstance.value.render()
  }
}

onMounted(() => {
  renderChart()
})

watch(
  () => props.data,
  (newData) => {
    renderChart()
  }
)

onBeforeUnmount(() => {
  if (chartInstance.value) {
    chartInstance.value.destroy()
  }
})
</script>

<style>
.apexcharts-xaxistooltip {
  background: transparent !important;
  border: none !important;
  color: #002665 !important;
  margin-top: 0px !important;
  padding-bottom: 0 !important;
  font-weight: bold !important;
}

.apexcharts-xaxistooltip-bottom:before {
  opacity: 0 !important;
}

.apexcharts-xaxistooltip-bottom:after {
  opacity: 0 !important;
}
</style>
