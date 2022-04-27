import { Component, OnInit } from '@angular/core';
import { Subscriber, Subscription } from 'rxjs';
import { IDeathRatesByState } from '../interfaces/ideath-rates-by-state';
import { IMaritalCountByState } from '../interfaces/imarital-count-by-state';
import { DeathRatesByStateService } from '../services/death-rates-by-state.service';
import { MaritalCountByStateService } from '../services/marital-count-by-state.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  constructor(private deathRatesByState: DeathRatesByStateService,
              private maritalCountByState: MaritalCountByStateService) { }

  dr_sub!: Subscription;
  mc_sub!: Subscription;

  table: boolean[] = [false, false, false];

  deathRates!: IDeathRatesByState[];
  maritalCount!: IMaritalCountByState[];
  errorMessage: string = "";

  backId: number = 0;
  bckgrdColors: string[] = ["#fff", "#ccc"];

  ngOnInit(): void {
    // this.dr_sub = this.deathRatesByState.getDeathRates().subscribe({
    //   next: drs => this.deathRates = drs,
    //   error: err => this.errorMessage = err
    // });

    this.mc_sub= this.maritalCountByState.getMaritalCount().subscribe({
      next: mc => this.maritalCount = mc,
      error: err => this.errorMessage = err
    })
  }

  setTable(idx: number): void {
    this.table = [false, false, false];
    this.table[idx] = true;
    console.log(this.table);
  }

  alternateBackgroundColor(): string {
    return this.bckgrdColors[this.backId == 0 ? this.backId++ : this.backId--]
  }

  // return a string to include trailing zeros
  deathRateAdjust(death_rate: number): string {
    return (death_rate * 100).toFixed(2);
  }

  ngOnDestroy(): void {
    this.dr_sub.unsubscribe();
    this.mc_sub.unsubscribe();
  }
}
