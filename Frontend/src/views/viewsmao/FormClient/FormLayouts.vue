<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import BasicHeaderForm from "@/components/dashboardmao/fom/BasicHeaderForm.vue";
import BasicLayout from '@/components/forms/form-horizontal/BasicLayout.vue';
import FormSeprator from '@/components/dashboardmao/fom/FormSeprator.vue';
import BasicWithIcons from '@/components/dashboardmao/fom/BasicWithIcons.vue'; 

// theme breadcrumb
const page = ref({ title: 'Satisfaccion al Cliente' });
const breadcrumbs = ref([
    {
        text: 'Satisfaccion al Cliente',
        disabled: false,
        href: '#'
    },
    {
        text: 'Formularios',
        disabled: true,
        href: '#'
    }
]);

</script>
<template>
   <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
   <v-row>
        
        <v-col cols="12" sm="10" md="6">
            <UiParentCard title="Calificanos">
                <BasicLayout/>
            </UiParentCard>           
        </v-col>

        <v-col cols="12" md="6">
            <UiParentCard title="Queja / Sugerencia">
                <BasicWithIcons/>
            </UiParentCard>           
        </v-col>
        <v-col cols="12">
            <FormSeprator/>        
        </v-col>

   </v-row>           
</template>