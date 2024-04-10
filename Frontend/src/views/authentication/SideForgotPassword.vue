<script setup lang="ts">
import Logo from '@/layouts/full/logo/Logo.vue';
/* Reset form */
import ResetPassword from '@/components/auth/ResetForm.vue';
</script>

<template>
    <div class="pa-3">
        <v-row class="h-100vh mh-100 auth">
            <v-col cols="12" lg="8" xl="8" xxl="9" class="d-lg-flex align-center justify-center authentication position-relative">
               
                <div class="">
                    <img src="@/assets/images/logos/bulls logo.png" height="450" class="position-relative d-none d-lg-flex" alt="login-background" />
                </div>
            </v-col>
            <v-col cols="12" lg="4" xl="4" xxl="3" class="d-flex align-center justify-center bg-surface">
                <div class="pa-sm-7 pa-4">
                    <h2 class="text--darken-2 text-h4 font-weight-semibold">¿Olvido su contraseña?</h2>
                    <p class="text-subtitle-1 text-medium-emphasis py-4 text-10">
                        Ingrese la dirección de correo electrónico asociada con su cuenta y le enviaremos un enlace por correo electrónico para restablecer su contraseña.
                    </p>
                    <ResetPassword />
                    <v-btn size="large" color="lightprimary" to="/auth/login" block class="mt-5 text-primary" flat>Regresar al login</v-btn>
                </div>
            </v-col>
        </v-row>
    </div>
</template>
