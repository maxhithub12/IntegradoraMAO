<script setup lang="ts">
import { ref } from "vue";

import { useDate } from 'vuetify'
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import FullCalendar from '@/views/apps/calendar/calCLi/FullCalender.vue';
const date = ref(new Date());
const seldate = ref(new Date('2018-03-02'))
const adapter = useDate()

function allowedDates(val: unknown) {
    return parseInt(adapter.toISO(val).split('-')[2], 10) % 2 === 0
}
const page = ref({ title: "Calendario Clientes" });
const breadcrumbs = ref([
    {
        text: "Calendario",
        disabled: false,
        href: "#",
    },
    {
        text: "Calendario Clientes",
        disabled: true,
        href: "#",
    },
]);
</script>

<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
        <v-col cols="12">
            <UiParentCard title="Calendario Clientes">
                <FullCalendar />
            </UiParentCard>
        </v-col>
       
    </v-row>
</template>
