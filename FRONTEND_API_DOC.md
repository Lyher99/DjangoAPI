# Frontend API Docs (DjangoAPI)

This guide is for frontend developers who want to connect to this Django REST API quickly.

## 1) Base URL

Use this during local development:

- `http://127.0.0.1:8000/api/`

Notes:
- The same routes are also mounted at root (`/`) in this project.
- For consistency, use the `/api/` prefix in frontend code.

## 2) Authentication

- No authentication is required right now.
- All endpoints are public.

## 3) CORS (local frontend allowed origins)

These frontend origins are allowed by backend settings:

- `http://127.0.0.1:5500`
- `http://localhost:5500`
- `http://127.0.0.1:3000`
- `http://localhost:3000`
- `http://127.0.0.1:5173`
- `http://localhost:5173`

## 4) Category API

### GET all categories

- Method: `GET`
- URL: `/api/APICategory/`

Example:

```http
GET http://127.0.0.1:8000/api/APICategory/
```

Response item shape:

```json
{
  "id": 1,
  "categoryName": "Shoes",
  "categoryImage": "/media/images/Categories/shoes.png"
}
```

### POST create category

- Method: `POST`
- URL: `/api/APICategory/`
- Content-Type: `multipart/form-data` (recommended when uploading image)

Form fields:

- `categoryName` (string)
- `categoryImage` (file, optional)

### GET one category

- Method: `GET`
- URL: `/api/APICategory/{id}/`

### PUT update category

- Method: `PUT`
- URL: `/api/APICategory/{id}/`

### DELETE category

- Method: `DELETE`
- URL: `/api/APICategory/{id}/`

## 5) Product API

### GET all products

- Method: `GET`
- URL: `/api/APIProduct/`

Example:

```http
GET http://127.0.0.1:8000/api/APIProduct/
```

Response item shape:

```json
{
  "id": 1,
  "productName": "Running Shoes",
  "price": "99.99",
  "productImage": "/media/images/Products/shoe1.png",
  "productDate": "2026-04-05T05:20:11.210Z",
  "categoryID": 1,
  "productDescript": "<p>Lightweight and comfortable.</p>",
  "weight": "1kg",
  "availability": "In stock",
  "shipping": "Free shipping"
}
```

### POST create product

- Method: `POST`
- URL: `/api/APIProduct/`
- Content-Type: `multipart/form-data` (recommended for image upload)

Form fields:

- `productName` (string)
- `price` (string)
- `productImage` (file, optional)
- `categoryID` (number, Category id)
- `productDescript` (string, HTML allowed)
- `weight` (string)
- `availability` (string)
- `shipping` (string)

### GET one product

- Method: `GET`
- URL: `/api/APIProduct/{id}/`

### PUT update product

- Method: `PUT`
- URL: `/api/APIProduct/{id}/`

### DELETE product

- Method: `DELETE`
- URL: `/api/APIProduct/{id}/`

## 6) Frontend Fetch Examples

### Get products

```js
const res = await fetch("http://127.0.0.1:8000/api/APIProduct/");
const products = await res.json();
console.log(products);
```

### Create product with image

```js
const formData = new FormData();
formData.append("productName", "Running Shoes");
formData.append("price", "99.99");
formData.append("categoryID", "1");
formData.append("productDescript", "<p>Lightweight and comfortable.</p>");
formData.append("weight", "1kg");
formData.append("availability", "In stock");
formData.append("shipping", "Free shipping");
formData.append("productImage", fileInput.files[0]);

const res = await fetch("http://127.0.0.1:8000/api/APIProduct/", {
  method: "POST",
  body: formData
});

const created = await res.json();
console.log(created);
```

## 7) Media/Image URL Handling

Image fields (`productImage`, `categoryImage`) usually return URLs like:

- `/media/images/Products/your-file.png`
- `/media/images/Categories/your-file.png`

In frontend apps, build full URL when needed:

```js
const apiHost = "http://127.0.0.1:8000";
const fullImageUrl = `${apiHost}${product.productImage}`;
```

## 8) Common Errors

- `404 Not Found`: Wrong URL path or wrong id.
- `400 Bad Request`: Missing required fields or invalid field types.
- CORS error in browser: frontend origin not in allowed list.

## 9) Quick Test URLs

- Home: `http://127.0.0.1:8000/`
- Products API: `http://127.0.0.1:8000/api/APIProduct/`
- Categories API: `http://127.0.0.1:8000/api/APICategory/`
