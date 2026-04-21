export interface Category{
    id: number;
    name: string
}

export interface Product {
  id: number;
  product_name: string;
  price: number;
  Category: number;
  isActiv: boolean;
}

export interface User{
    id: number;
    name: string;
    email: string; //lname, fname elsi dobawish!
}

export interface Review{
    id: number;
    product: number; //FKey na product
    user: User; 
    rating: number;
    comment: string;
}

export interface OrderItem{
    id: number;
    name: string;
    quantity: number;
}

export interface Order{
    id: number;
    user: User;
    created_at: string;
    total_price: number;
    items: OrderItem[] //spisok tovarov v zakaze
}