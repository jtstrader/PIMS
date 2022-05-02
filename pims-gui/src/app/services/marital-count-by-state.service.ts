import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { IMaritalCountByState } from '../interfaces/imarital-count-by-state';

@Injectable({
  providedIn: 'root'
})
export class MaritalCountByStateService {

  constructor(private http: HttpClient) { }
  private url: string = "http://localhost:8080/api/marital_status/couples" 

  getMaritalCount(): Observable<IMaritalCountByState[]> {
    // sample result: ["FL, 0.160220", "GA, 0.039402"]
    return this.http.get<String[]>(this.url).pipe(map(result => {
      let ret: IMaritalCountByState[] = result.map(x => {
        return {
          name: x.split(",")[0], 
          value: Number(x.split(",")[1])
        };
      });
      console.log(ret);
      return ret;
    }),
    catchError(this.handleError));
  }

  private handleError(err: HttpErrorResponse) {
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
      errorMessage = `An error occured: ${err.error.message}`;
    } else {
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    return throwError(() => errorMessage);
  }
}
