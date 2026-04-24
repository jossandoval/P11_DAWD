import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, mapTo } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class WebService {
  private readonly apiUrl = 'https://jsonplaceholder.typicode.com/posts/1';

  constructor(private http: HttpClient) {}

  testConnection(): Observable<boolean> {
    return this.http.get(this.apiUrl).pipe(
      mapTo(true),
      catchError(() => of(false))
    );
  }
}
