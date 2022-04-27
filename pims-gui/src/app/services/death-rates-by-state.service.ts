import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { IDeathRatesByState } from '../interfaces/ideath-rates-by-state';

@Injectable({
  providedIn: 'root'
})
export class DeathRatesByStateService {

  constructor(private http: HttpClient) { }
  private url: string = "http://localhost:8080/api/health/death_rate";

  getDeathRates(): Observable<IDeathRatesByState[]> {
    return this.http.get<String[]>(this.url).pipe(map(result => {
      let ret: IDeathRatesByState[] = [];
      for (let x of result) {
        ret.push(
          {state_abbr: x.split(",")[0], death_rate: Number(x.split(",")[1])}
        )
      }
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
