import { Routes } from '@angular/router';
import { Menu } from './components/menu/menu';
import { Login} from './components/login/login';
import { Calories } from './components/calories/calories';
import { Register } from './components/register/register';

//местный тугис
export const routes: Routes = [
    { path: 'menu', component: Menu },
    { path: 'login', component: Login },
    { path: 'register', component: Register },
    { path: 'calories', component: Calories },
    { path: '', redirectTo: 'menu', pathMatch: 'full' },
    { path: '**', redirectTo: 'menu' }
];