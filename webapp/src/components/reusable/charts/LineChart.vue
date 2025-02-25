<template>
  <div id="line-chart" class="px-2 pt-4"></div>
</template>
<script lang="ts" setup>
import { onMounted } from "vue"
import ApexCharts from "apexcharts"
import type { BarData } from "@/type"

const props = defineProps<{
  chartData: BarData[]
}>()

onMounted(() => {
  const options = {
    series: [
      {
        name: "Average Chemicals",
        data: [
          { x: "1/10", y: 4 },
          { x: "2/10", y: 3 },
          { x: "3/10", y: 10 },
          { x: "4/10", y: 9 },
          { x: "5/10", y: 5 },
          { x: "6/10", y: 29 },
          { x: "7/10", y: 20 },
          { x: "8/10", y: 4 },
          { x: "19/10", y: 32 },
          { x: "10/10", y: 9 },
          { x: "11/10", y: 29 },
          { x: "12/10", y: 9 },
          { x: "13/10", y: 19 },
        ],
      },
    ],
    chart: {
      height: "100%",
      type: "line",
      toolbar: {
        show: false,
        tools: {
          download: false,
          selection: false,
          zoom: false,
          zoomin: false,
          zoomout: false,
          pan: false,
          reset: false,
          customIcons: [],
        },
      },
    },
    stroke: {
      width: 5,
      curve: "smooth",
    },
    xaxis: {
      type: "category",
      labels: {
        show: true,
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
      type: "gradient",
      gradient: {
        shade: "dark",
        gradientToColors: ["#002665"],
        shadeIntensity: 1,
        type: "vertical",
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 100, 100, 100],
      },
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
          '<div class="p-1.5 rounded-lg bg-black/80 text-white text-xs"> Average : ' +
          data.y +
          "</div>"
        )
      },
    },
  }

  if (
    document.getElementById("line-chart") &&
    typeof ApexCharts !== "undefined"
  ) {
    const chart = new ApexCharts(document.getElementById("line-chart"), options)
    chart.render()
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
