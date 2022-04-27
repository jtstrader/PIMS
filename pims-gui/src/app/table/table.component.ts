import { Component, OnInit } from '@angular/core';
import { Subscriber, Subscription } from 'rxjs';
import { IDeathRatesByState } from '../interfaces/ideath-rates-by-state';
import { DeathRatesByStateService } from '../services/death-rates-by-state.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  constructor(private deathRatesByState: DeathRatesByStateService) { }

  sub!: Subscription;
  deathRates!: IDeathRatesByState[];
  errorMessage: string = "";

  ngOnInit(): void {
    this.sub = this.deathRatesByState.getDeathRates().subscribe({
      next: drs => this.deathRates = drs,
      error: err => this.errorMessage = err
    });
  }

}
