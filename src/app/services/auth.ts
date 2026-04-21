import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';
import { Router } from '@angular/router';

const API = 'http://localhost:8000/api/auth';//сюда отправляем чтобы залогиниться

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(private http: HttpClient, private router: Router) {}

  login(username: string, password: string) {
    return this.http.post<{ token: string }>(
      `${API}/login/`,
      { username, password }
    ).pipe(
      tap(res => localStorage.setItem('token', res.token))
    );
  }

  register(username: string, password: string, email: string) {
  return this.http.post(`${API}/register/`, { 
    username, 
    password,
    email,
    passwordRavno: password  //чтобы убедиться что ты не воздухан
  });
}
  logout() {
    return this.http.post(`${API}/logout/`, {}).pipe(
      tap(() => {
        localStorage.removeItem('token');
        this.router.navigate(['/login']);
      })
    );
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }
}