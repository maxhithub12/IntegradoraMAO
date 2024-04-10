<script setup lang="ts">
import { ref } from "vue";
import { useTheme } from 'vuetify';
import { getPrimary, getSecondary } from '@/utils/UpdateColors';
import BaseBreadcrumb from "@/components/shared/BaseBreadcrumb.vue";
import RevenueUpdates from "@/components/dashboardmao/modern/RevenueUpdates.vue";

import UiParentCard from '@/components/shared/UiParentCard.vue';
import UiChildCard from '@/components/shared/UiChildCard.vue';

import BasicLayout from '@/components/forms/form-horizontal/BasicLayout.vue';
import { computed } from 'vue';







const page = ref({ title: "Satifaccion al Cliente" });
const breadcrumbs = ref([
    {
        text: "Dashboards",
        disabled: false,
        href: "#",
    },
    {
        text: "Satisfacción al cliente",
        disabled: true,
        href: "#",
    },
]);

const theme = useTheme();
const success = theme.current.value.colors.success;
const accent = theme.current.value.colors.accent;
const warning = theme.current.value.colors.warning;

/*Donut chart*/
const donutchartOptions = computed(() => {
    return {
        chart: {
            type: 'donut',
            height: 300,
            fontFamily: `inherit`,
            foreColor: '#adb0bb',
        },
        dataLabels: {
            enabled: false
        },
        plotOptions: {
            pie: {
                donut: {
                    size: '70px'
                }
            }
        },
        legend: {
            show: true,
            position: 'bottom',
            width: '50px'
        },
        colors: ['#6ac3fd', '#0b70fb', '#f64e60', '#26c6da', '#ffa800'],
        responsive: [
            {
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        ]
    };
});
const donutChart = {
    series: [44, 55, 41, 17, 15]
};
const piechartOptions = computed(() => {
    return {
        chart: {
            type: 'pie',
            height: 300,
            fontFamily: `inherit`,
            foreColor: '#adb0bb',
            toolbar: {
                show: false
            }
        },
        dataLabels: {
            enabled: false
        },
        plotOptions: {
            pie: {
                donut: {
                    size: '70px'
                }
            }
        },
        legend: {
            show: true,
            position: 'bottom',
            width: '50px'
        },
        colors: ['#6ac3fd', '#0b70fb', '#f64e60', '#26c6da', '#ffa800'],
        tooltip: {
            fillSeriesColor: false
        },
        labels: ['Excelemte', 'Bueno', 'Regular', 'Malo', 'Muy Malo'],
        responsive: [
            {
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        ]
    };
});
const pieChart = {
    series: [44, 55, 13, 43, 22]
};

/*Area chart */
const chartOptions = computed(() => {
    return {
        chart: {
            type: 'area',
            height: 300,
            fontFamily: `inherit`,
            foreColor: '#adb0bb',
            zoom: {
                enabled: true
            },
            toolbar: {
                show: false
            }
        },
        colors: [getPrimary.value,getSecondary.value],
        dataLabels: {
            enabled: false
        },
        stroke: {
            width: '3',
            curve: 'smooth'
        },
        xaxis: {
            type: 'datetime',
            categories: [
                '2018-09-19T00:00:00',
                '2018-09-19T01:30:00',
                '2018-09-19T02:30:00',
                '2018-09-19T03:30:00',
                '2018-09-19T04:30:00',
                '2018-09-19T05:30:00',
                '2018-09-19T06:30:00',
            ]
        },
        yaxis: {
            opposite: false,
            labels: {
                show: true
            }
        },
        legend: {
            show: true,
            position: 'bottom',
            width: '50px'
        },
        grid: {
            show: false
        },
        tooltip: {
            theme: 'dark',
        }
    };
});
const areaChart = {
    series: [
        {
            name: 'Clientes Satisfechos',
            data: [31, 39, 53, 63, 70, 109, 100]
        },
        {
            name: 'Clientes Insatisfechos',
            data: [9, 13, 19, 23, 30, 15, 32]
        }
    ]
};

/*Colum chart */
const chartOptionsColum = computed(() => {
    return {
        chart: {
            type: 'bar',
            height: 350,
            fontFamily: `inherit`,
            foreColor: '#adb0bb',
            toolbar: {
              show: false,
            },
        },
        colors: ['#dd0000', '#0b70fb', '#f64e60'],
        plotOptions: {
            bar: {
                horizontal: false,
                endingShape: 'rounded',
                columnWidth: '20%'
            }
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            show: true,
            width: 2,
            colors: ['transparent']
        },

        xaxis: {
            categories: ['Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiempre', 'Octubre']
        },
        yaxis: {
          title: {
            text: '',
          },
        },
        fill: {
            opacity: 1
        },
       
        tooltip: {
            theme: 'dark',
            y: {
              formatter(val:any) {
                return ` ${val} `;
              },
            },
        },
        grid: {
          show: false,
        },
        legend: {
          show: true,
          position: 'bottom',
          width: '50px',
        },
        responsive: [
            {
                breakpoint: 600,
                options: {
                    yaxis: {
                        show: false
                    }
                }
            }
        ]
    };
});
const columnChart = {
    series: [
        {
            name: 'Quejas',
            data: [32, 12, 24, 11, 32, 16, 7, 21, 45]
        },
        {
            name: 'Sugerencias',
            data: [56, 75, 91, 78, 57, 75, 71, 87, 74]
        },
     
    ]
};


</script>

<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
       

        <v-col cols="12">
            <UiParentCard title="Usuarios Satisfechos">
                <apexchart type="area" height="300" :options="chartOptions" :series="areaChart.series"> </apexchart>
            </UiParentCard>
        </v-col>

        <v-col cols="12">
            <v-row>
                <v-col cols="12" lg="6">
                    <!-- ---------------------------------------------------- -->
                    <!-- Donut Chart -->
                    <!-- ---------------------------------------------------- -->
                    <UiChildCard title="Opiniones de Usuario" class="bg-surface">
                        <apexchart type="donut" height="300" :options="donutchartOptions" :series="donutChart.series"> </apexchart>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" lg="6">
                    <!-- ---------------------------------------------------- -->
                    <!-- Pie Chart -->
                    <!-- ---------------------------------------------------- -->
                    <UiChildCard title="Puntuaciones de Usuarios" class="bg-surface">
                        <apexchart type="pie" height="300" :options="piechartOptions" :series="pieChart.series"> </apexchart>
                    </UiChildCard>
                </v-col>
            </v-row>
        </v-col>

        <v-col cols="12">
            <UiParentCard title="Quejas & Sugerencias">
                <apexchart type="bar" height="300" :options="chartOptionsColum" :series="columnChart.series"> </apexchart>
            </UiParentCard>
        </v-col>

    </v-row>
    
</template>
