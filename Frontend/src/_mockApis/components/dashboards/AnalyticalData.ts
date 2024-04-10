import type { myContacts, projectTable, weeklyStates, dailyActivities } from '@/types/components/dashboards/AnalyticalDash';
import { MessageDotsIcon, ShoppingCartIcon, StarIcon } from 'vue-tabler-icons';
import img1 from '@/assets/images/profile/1.jpg';
import img2 from '@/assets/images/profile/2.jpg';
import img3 from '@/assets/images/profile/3.jpg';
import img4 from '@/assets/images/profile/4.jpg';
import img5 from '@/assets/images/profile/5.jpg';
/*--Blog Cards--*/
const myContactsData: myContacts[] = [
  {
    title: "Pavan Kumar",
    avatar: img1,
    avatarstatus: "success",
    desc: "info@wrappixel.com",
  },
  {
    title: "Sonu Nigam",
    avatar: img2,
    avatarstatus: "error",
    desc: "pamela1987@gmail.com",
  },
  {
    title: "Arijit singh",
    avatar: img3,
    avatarstatus: " ",
    desc: "cruise1298.fiplip@gmail.com",
  },
  {
    title: "Pavan Kumar",
    avatar: img4,
    avatarstatus: "success",
    desc: "kat@gmail.com",
  },
];

const projectTableData: projectTable[] = [
  {
    img: img1,
    activestate: "",
    leadname: "Sunil Joshi",
    leademail: "",
    projectname: "Falta de arención a primerizos",
    statuscolor: "success",
    statustext: "Resuelto",
    money: "Queja",
  },
  {
    img: img2,
    activestate: "active",
    leadname: "Andrew",
    leademail: "",
    projectname: "Bañeras con ropa sucia",
    statuscolor: "success",
    statustext: "Resuelto",
    money: "Queja",
  },
  {
    img: img3,
    activestate: "",
    leadname: "Nirav Joshi",
    leademail: "",
    projectname: "Actualizar equipos",
    statuscolor: "error",
    statustext: "Pendiente",
    money: "Sugerencia",
  },
  {
    img: img4,
    activestate: "",
    leadname: "Nirav Joshi",
    leademail: "",
    projectname: "Aumentar el espacio",
    statuscolor: "error",
    statustext: "Pendiente",
    money: "Sugerencia",
  },
  {
    img: img5,
    activestate: "",
    leadname: "Micheal Doe",
    leademail: "",
    projectname: "Cambiar el color del gimnasio",
    statuscolor: "warning",
    statustext: "En proceso",
    money: "Sugerencia",
  },
];

const weeklyStatesData: weeklyStates[] = [
  {
    color: "primary",
    icon: ShoppingCartIcon,
    title: "Top Sales",
    desc: "Johnathan Doe",
    percent: 68,
  },
  {
    color: "warning",
    icon: StarIcon,
    title: "Best Seller",
    desc: "MaterialPro Admin",
    percent: 45,
  },
  {
    color: "success",
    icon: MessageDotsIcon,
    title: "Most Commented",
    desc: "Ample Admin",
    percent: 10,
  },
]

const dailyActivitiesData: dailyActivities[] = [
  {
    color: "success",
    title: "Sesion 1",
    time: "04.05 AM"
  },
  {
    color: "primary",
    title: "Sesion 2",
    time: "04.25 AM"
  },
  {
    color: "secondary",
    title: "Sesion 3",
    time: "05.26 AM"
  },
  {
    color: "error",
    title: "Cardio",
    time: "05.12 AM"
  },
  {
    color: "error",
    title: "Salida",
    time: "06.23 AM"
  }

]

export { myContactsData, projectTableData, weeklyStatesData, dailyActivitiesData }