<template>
    <div id="scatter-plot"></div>
</template>
<script setup lang="ts">
import { onMounted } from 'vue';
import ApexCharts from 'apexcharts'
import type * as types from "@/type"

const props = defineProps<{
    dataSeries: types.Series[];
}>();

const colors = ['#9fd0f0', '#002665', '#644ab4']

onMounted(() => {

    const options = {
        series: props.dataSeries,
        chart: {
            height: "100%",
            type: "line",
            zoom: {
                enabled: false,
                allowMouseWheelZoom: false
            },
            toolbar: {
                show: false
            }
        },
        colors: colors,
        toolbar: {
            show: false
        },
        fill: {
            type: "solid"
        },
        grid: {
            show: false,
        },
        markers: {
            size: [3, 3, 3, 0, 0],
            colors: colors,
            strokeWidth: 0,
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
                    '<div class="p-1.5 bg-black/80 text-white text-xs"> Valeur Moyenne : ' +
                    data.y.toLocaleString('fr-BE', { maximumFractionDigits: 2 }) +
                    "</div>"
                )
            },
        },
        legend: {
            show: true,
            position: "bottom",
            itemMargin: {
                horizontal: 5, 
                vertical: 15
            },
            markers: {
                size: [3, 3, 3, 0, 0],
                colors: colors,
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

        },
        xaxis: {
            type: "numeric",
            tickAmount: 11,
            labels: {
                show: true,
                rotate: 0,
                rotateAlways: false,
                hideOverlappingLabels: false,
                formatter: (value: number) => Math.round(value),
                style: {
                    colors: "#D2D2D2",
                },
            },
            tooltip: {
                enabled: true,
            },
            axisTicks: {
                show: false,
            },
        },
        yaxis: {
            type: "numeric",
            labels: {
                formatter: (value: number) => value.toLocaleString('fr-BE', { maximumFractionDigits: 2 }),
            },
        },

    };

    if (document.getElementById("scatter-plot") && typeof ApexCharts !== 'undefined') {
        const chart = new ApexCharts(document.getElementById("scatter-plot"), options);
        chart.render();
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
    opacity: 0 !important
}

.apexcharts-xaxistooltip-bottom:after {
    opacity: 0 !important
}
</style>