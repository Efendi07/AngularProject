import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { Dashboard2Component } from './dashboard2/dashboard2.component';

const routes: Routes = [
  {path: "admin", component: AdminComponent},
  {path: "dashboard", component: DashboardComponent},
  {path: "dashboard2", component: Dashboard2Component},
  {path: "login", component: LoginComponent},
  {path: "", redirectTo:"login", pathMatch:"full" },
  {path: "register", component: RegisterComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
