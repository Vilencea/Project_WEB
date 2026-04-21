import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category, Product } from '../models/models';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private BASE_URL = 'http://127.0.0.1:8000/api';
  
  constructor(private http: HttpClient) { }

  //poluchaem vse product (burgery)
  getProducts(): Observable<Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/products/`);
  }


  //poluchaem categoryi!
  getCategories(): Observable<Category[]>{
    return this.http.get<Category[]>(`${this.BASE_URL}/category/`)
  }
}
