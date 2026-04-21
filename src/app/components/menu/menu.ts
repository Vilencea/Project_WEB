import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './menu.html',
  styleUrl: './menu.css',
})
export class Menu implements OnInit {
  searchText: string = '';
  maxPrice: number = 5000;
  products: any[] = [];
  categories: any[] = [];
  selectedCategoryId: number | null = null;
  cart: any[] = [];

  constructor(private http: HttpClient) {}

//методы фрейда дальше
  ngOnInit() {
    this.fetchCategories();
    this.fetchMenu();
  }
//запрашивает список категорий из апишки
  fetchCategories() {
    this.http.get<any[]>('http://127.0.0.1:8000/api/categories/').subscribe({
      next: (data) => {
        this.categories = data;
        console.log('Категории из API', data);
      },
      error: (err) => console.error('Ошибка загрузки категорий', err)
    });
  }

  fetchMenu() {
    this.http.get<any[]>('http://127.0.0.1:8000/api/products/').subscribe({
      next: (data) => {
      console.log('Продукты из API:', data);
      this.products = data;
    },
      error: (err) => console.error('Ошибка загрузки продуктов', err)
    });
  }
//когда хочешь чисто бургер покушать
  selectCategory(id: number | null) {
    this.selectedCategoryId = id;
  }
//возвращает только то, что соответствует
  isProductVisible(product: any): boolean {
  const matchesSearch = product.product_name.toLowerCase().includes(this.searchText.toLowerCase());
  const matchesPrice = product.price <= this.maxPrice;
  const matchesCategory = this.selectedCategoryId ? product.Category === this.selectedCategoryId : true;
  return matchesSearch && matchesPrice && matchesCategory;
}
//в корзину добавляет
  addToCart(product:any) {
    this.cart.push(product);
    alert(product.name + ' добавлен в корзину!');
  }
//удаляет продукт(капитан очевидность)
  deleteProduct(id: number) {
    this.products = this.products.filter(p => p.id !== id);
  }
//акшшан жок болганда басатын зат
  sortByPrice() {
    this.products.sort((a, b) => a.price - b.price);
  }
//фильтрларды сбрасывает
  resetFilter() {
    this.searchText = '';
    this.maxPrice = 2000;
  }
//очиститель
  clearCart() {
    this.cart = [];
  }
//акща санауды унатады
  getCartTotal() {
    return this.cart.reduce((sum, item) => sum + item.price, 0);
  }
}