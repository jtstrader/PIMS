import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError, map, Observable, throwError } from 'rxjs';
import { IPopulationDeathRatio } from '../interfaces/ipopulation-death-ratio';

@Injectable({
  providedIn: 'root'
})
export class PopulationDeathRatioService {

  constructor(private http: HttpClient) { }
  private url: string = "http://localhost:8080/api/health/death_ratio";

  getDeathRatio(): Observable<IPopulationDeathRatio[]> {
    return this.http.get<String[]>(this.url).pipe(map(result => {
      let ret: IPopulationDeathRatio[] = result.map(x => {
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
