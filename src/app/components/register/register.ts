import { Component } from '@angular/core';
import { AuthService } from '../../services/auth';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './register.html',
  styleUrls: ['./register.css']
})
export class Register {
  username = '';
  email = '';
  password = '';
  password2 = '';
  error = '';
  loading = false;

  constructor(
    private auth: AuthService,
    private router: Router
  ) {}

  onSubmit() {
    if (!this.username || !this.email || !this.password || !this.password2) return;
    if (this.password !== this.password2) {
      this.error = 'Пароли не совпадают';
      return;
    }
    this.loading = true;
    this.error = '';

    this.auth.register(this.username, this.password, this.email).subscribe({
      next: () => this.router.navigate(['/login']),
      error: err => {
        this.error = err.error?.username?.[0]
          ?? err.error?.email?.[0]
          ?? err.error?.password?.[0]
          ?? 'Дурыс емес, давай по новой';
        this.loading = false;
      }
    });
  }
}