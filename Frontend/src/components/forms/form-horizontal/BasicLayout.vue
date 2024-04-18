<script setup lang="ts">
import { ref } from "vue";
const rating5 = ref(3);
</script>
<template>
      <v-row >
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Nombre</v-label>
            <VTextField  type="text" placeholder="John Deo" hide-details ></VTextField>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Servicio</v-label>
            <VTextField  type="text" placeholder="Especifica que servicio" hide-details ></VTextField>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Email</v-label>
            <VTextField  type="email" placeholder="ejemplo@gmail.com" suffix="@example.com" hide-details ></VTextField>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Telefono</v-label>
            <VTextField  type="text" placeholder="412 2150 451" hide-details ></VTextField>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Mensaje</v-label>
             <VTextarea
                auto-grow
                placeholder="Cual es tu opinion?"
                rows="2"
                color="primary"
                row-height="25"
                shaped
                hide-details
            ></VTextarea>
        </v-col>
        <v-col>
            <v-label class=" font-weight-medium">Calificacion</v-label>
        </v-col>
        <v-col>
            <v-rating v-model="rating5" color="warning" hover density="compact"></v-rating>
        </v-col>
 
        <v-col cols="12" class="">
            <v-btn color="primary" flat>Enviar</v-btn>
        </v-col>
    </v-row>
</template>
